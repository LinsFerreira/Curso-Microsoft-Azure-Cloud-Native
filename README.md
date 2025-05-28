# Curso-Microsoft-Azure-Cloud-Native

**Azure Cloud Native – Conceitos Fundamentais**

**1. Cloud Native**

Refere-se ao desenvolvimento de aplicações que aproveitam ao máximo os recursos da nuvem, como escalabilidade automática, resiliência e implantação contínua.
No Azure, isso significa usar serviços gerenciados e arquiteturas modernas como microsserviços e contêineres.

**2. Azure Kubernetes Service (AKS)**

Serviço gerenciado de Kubernetes no Azure.
Permite orquestrar contêineres com facilidade, escalar aplicações automaticamente e integrar com outros serviços do Azure.

**3. Azure App Service**

Plataforma para hospedar aplicações web, APIs REST e backends móveis.
Suporta várias linguagens (como .NET, Java, Node.js, Python) e oferece escalabilidade automática e integração contínua.

**4. Azure Functions**

Serviço de computação serverless.
Executa código sob demanda em resposta a eventos, sem necessidade de gerenciar infraestrutura.

**5. Azure DevOps / GitHub Actions**

Ferramentas para CI/CD (Integração e Entrega Contínuas).
Automatizam testes, builds e deploys de aplicações cloud native.

**6. Azure Container Registry (ACR)**

Repositório privado para armazenar e gerenciar imagens de contêineres Docker.
Integrado com AKS e outros serviços de contêiner.

**7. Infraestrutura como Código (IaC)**

Uso de ferramentas como Bicep, ARM Templates ou Terraform para definir e provisionar recursos do Azure de forma automatizada e reprodutível.

**8. Observabilidade**

Monitoramento com Azure Monitor, Application Insights e Log Analytics para rastrear desempenho, detectar falhas e gerar insights.

Aqui está um diagrama visual que mostra como os principais conceitos do Azure Cloud Native se conectam em uma arquitetura moderna:

![image](https://github.com/user-attachments/assets/051bb2bf-5b81-4d3b-8704-ff104b59182f)

**Destaques do Diagrama:**

**Cloud Native** é o ponto central, conectando-se a serviços como AKS, App Service e Functions.  
**AKS** se integra ao Azure Container Registry (ACR) para armazenar imagens de contêiner.  
**App Service** e **Functions** se conectam ao pipeline de DevOps/GitHub Actions.  
**IaC** é usado para provisionar toda a infraestrutura.  
**Observabilidade** monitora os principais serviços em execução.  



