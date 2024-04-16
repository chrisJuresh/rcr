from viewflow import this
from viewflow.workflow import flow, act
from viewflow.workflow.flow import views
from .models import JDProcess

class JDFlow(flow.Flow):
    process_class = JDProcess

    start = (
        flow.Start(views.CreateProcessView.as_view(fields=["jd"]))
        .Next(this.submitted)
    )

    submit = (
        flow.View(views.UpdateProcessView.as_view(fields=["submitted"]))
        .Next(this.rcr_review)
    )

    rcr_review = (
    flow.View(views.UpdateProcessView.as_view(fields=["rcr_approved"]))
    .Next(this.check_rcr_approval)
    )

    check_rcr_approval = (
    flow.If(act.process.rcr_approved)
    .Then(this.rsa_review)
    .Else(this.rcr_ammendments)
    )

    rcr_ammendments = (
    flow.View(views.UpdateProcessView.as_view(fields=["ammended"]))
    .Next(this.rcr_review)
    )

    rsa_review = (
    flow.View(views.UpdateProcessView.as_view(fields=["rsa_approved"]))
    .Next(this.check_rsa_approval)
    )

    check_rsa_approval = (
    flow.If(act.process.rsa_approved)
    .Then(this.end)
    .Else(this.rsa_ammendments)
    )

    rsa_ammendments = (
    flow.View(views.UpdateProcessView.as_view(fields=["ammended"]))
    .Next(this.rsa_review)
    )

    end = flow.End()

    def start_process(self, activation, jd):
        activation.process.jd = jd
        activation.process.save()  # Ensuring the process instance is saved
        return activation.process