from django.db import models
from trusts.models import Trust
from specialities.models import ConsultantType, Speciality
from users.models import User
from simple_history.models import HistoricalRecords 
from transitions.extensions import GraphMachine as Machine
from django.core.files import File 


class JD(models.Model):
    file = models.FileField(upload_to='JDs/')
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE)

    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE)

    primary_specialities = models.ManyToManyField(Speciality, related_name='primary_specialities')
    sub_specialities = models.ManyToManyField(Speciality, related_name='sub_specialities', blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_jds')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='reviewed_jds')

    requirements_met = models.BooleanField(default=False)

    history = HistoricalRecords() 

    status = models.CharField(max_length=50, default='Init')
    status_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    diagram = models.ImageField(upload_to='JDs/', blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_machine = JDStateMachine(self)

    def update_state(self, event):
        self.status = event.state.name
        image_path = f'JDs/{self.id}.png'
        self.get_graph().draw(image_path, prog='dot')

        with open(image_path, 'rb') as img_file:
            self.diagram.save(f'state_{self.id}.png', File(img_file), save=True)

        self.save()

        def __str__(self):
            return str(self.id)

class JDStateMachine:
    def __init__(self, jd):
        self.jd = jd
        states = ['Init', 'Draft', 'Trust Submitted', 'RCR approved', 'RSA approved', 'RCR rejected', 'RSA rejected']
        transitions = [
            ['create', 'Init', 'Draft'],
            ['submit', 'Draft', 'Trust Submitted'],

            ['reject', 'Trust Submitted', 'RCR rejected'],
            ['ammend', 'RCR rejected', 'Trust Submitted'],
            ['approve', 'Trust Submitted', 'RCR approved'],

            ['reject', 'RCR approved', 'RSA rejected'],       
            ['ammend', 'RSA rejected', 'RCR approved'],     
            ['approve', 'RCR approved', 'RSA approved'],
 
        ]
        
        self.machine = Machine(model=self.jd, states=states, transitions=transitions, initial=self.jd.status, send_event=True, after_state_change='update_state')

class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class ChecklistQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    consultant_type = models.ForeignKey(ConsultantType, on_delete=models.CASCADE, related_name='checklist_questions')
    
    required = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.consultant_type.name}: {self.question.text}"
    

class ChecklistAnswer(models.Model):
    jd = models.ForeignKey(JD, on_delete=models.CASCADE, related_name='checklist_answers')
    checklist_question = models.ForeignKey(ChecklistQuestion, on_delete=models.CASCADE, related_name='checklist_answers')

    present = models.BooleanField(default=False)
    page_numbers = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Answer to {self.checklist_question.question} for JD {self.jd.id}"
