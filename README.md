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

**O que é o GitHub Copilot?**

O GitHub Copilot é um assistente de codificação de IA que ajuda você a escrever código mais rápido e com menos esforço, permitindo que você concentre mais energia na resolução de problemas e na colaboração.

Foi comprovado que o GitHub Copilot aumenta a produtividade dos desenvolvedores e acelera o ritmo de desenvolvimento de software.

**Recursos do Copilot**

O GitHub Copilot inclui um conjunto de recursos. Você pode usar o Copilot para:

* Obtenha sugestões de código conforme você digita em seu IDE
* Converse com o Copilot para pedir ajuda com seu código
* Peça ajuda ao Copilot para usar a linha de comando
* Organize e compartilhe o contexto específico da tarefa com o Copilot Spaces para obter respostas mais relevantes
* Gerar uma descrição das alterações em uma solicitação de pull (somente Copilot Enterprise)
* Crie e gerencie coleções de documentação, chamadas bases de conhecimento, para usar como contexto para conversar com o Copilot (somente Copilot Enterprise)
* Trabalhe nas alterações do código e crie uma solicitação de pull para você revisar (somente Copilot Pro+ e Copilot Enterprise)

O copiloto está disponível:

* No seu IDE
* No GitHub Mobile, como uma interface de bate-papo
* No Windows Terminal Canary, por meio da interface de bate-papo do Terminal
* Na linha de comando, por meio do GitHub CLI
* No site do GitHub

