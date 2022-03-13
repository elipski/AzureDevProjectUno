# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

Comparing between VM and Azure Web App of cost, scalability and availablity. To make this comparision I 
sected a VM build and App Service plan that we as close to comperable betwen RAM, Cores, and vCPU.

## VM based Web App
Standard Tier 1 D4 v3 (4 vCPUs, 16 GB RAM)  
 - The monthy cost for a single basic lunix based VM is: $170.87 *,**
 - Manaual Scalability unless we made the VM part of a scale set for an additional cost
 - Availability would be impacted by deployments and traffic peaks that exeeded the performace limits of the app.

##App Service App
Standard Tier; 1 S3 4 Core(s), 7 GB RAM, 50 GB Storage
 - The monthly cost for single linux based app service is: $277.40 *,**
 - Automatic scalability (assumes the App remains stateless)
 - Availability would not be impacted by deployments. Automatic scaling would provide availablity through traffic spikes

There are stark differences between using and App Service and a clasic VM in Azure, however the least
important of these differnces is cost. To determine the appropriate platform for your app depends on the 
technical and non-technical performance characteristics that is expected from a your Web based application.

Web app based infrastructure povides an easy platform to deploy an app becuase it removes the need to manage the underlying 
infrastructure (i.e. the VM and associated OS maintenance). This is called Platform as a service (PaaS). Takiing away the 
management of an underlying VM (cloud or on-prem) relieves very big operational burden from any enterprise reposnsible 
for building and deploying Web based appications.   

* Using Azure price estimator I came up with the following costs for VM and App Service
** All pricing is based on 100% availability (730 hours/month)


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 