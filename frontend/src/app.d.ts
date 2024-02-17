// app.d.ts
declare global {
	// src/app.d.ts
	declare namespace App {
		interface Locals {
			user?: any; // Or a more specific type if you have one
		}
	}
}

export {};
