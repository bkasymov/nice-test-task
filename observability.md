# **Access and Stakeholders**

| **Role**                      | **Access and Responsibilities**                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------|
| **Production Support Engineers**| Have access to tracing tools to check clients' traces.                                                |
| **Developers**                 | Can check their transactions via traces and logs (using tools like Grafana and Datadog).               |
| **DevOps Engineers**           | Use dashboards (e.g., Grafana) to monitor system health and performance.                              |
| **All Engineers**              | Receive alerts based on their roles and work environments, ensuring that the right team is informed.  |

---

# **Best Practices**

It is best practice to install **SSO (Single Sign-On)** on each corporate application to manage authentication and authorization. For example, you can set expiration dates for accesses to systems like **Grafana**.

---

# **Access to Tracing Tools**

- **Production Support Engineers**: Access tracing tools to monitor and verify client traces.
- **Developers**: Check transaction logs and traces via platforms like **Grafana** and **Datadog**.
- **DevOps Engineers**: Monitor overall system performance through **Grafana dashboards**.

### Alerts:
Alerts should be configured based on the engineers' roles and their respective work environments, ensuring that they receive the relevant notifications.


# **Logging**
Before setting up logging, it's important to define:
- **What kinds of logs** we need
- **How long** we will retain them
- **Where** they will be stored
- **Who** will have access to them

### Types of logs to include:
- **VM logs**: RAM, CPU, disk storage, networks
- **Kubernetes logs**: nodes, pods, network
- **Ingress controller logs**: NGINX, Istio, Traefik, etc.
- **Other logs**: Any additional logs required for business operations

### Common tools:
- **Prometheus**: Popular for log monitoring
- **CLI tools**: Useful for real-time log access on VMs (e.g., NGINX logs)
- **Data Lakes**: For storing large volumes of logs

---

# **Tracing**
When working with **CloudRun** (connected to **Google Cloud Trace**), clients can observe:
- **Canceled queries**
- **Errors**
- **Other performance issues**

For open-source solutions:
- **Datadog**: More useful for backend transaction monitoring
- **Jaeger** and **Zipkin**: Known tracing tools, though I haven't worked with them yet

---

# **Metrics Collection**
The most common tool for metrics collection is **Prometheus**, which integrates with:
- Application logs
- NGINX (or other load balancer) logs
- OS traces

### Scaling up:
As the infrastructure grows with more VMs and devices, it's advisable to use **VictoriaMetrics**:
- Supports **multi-clusters**
- Queries are **load-balanced** across VMs

Other tools like **ELK**, **DataLake (Azure)** can also be used depending on the company's size and requirements.

---

# **Dashboarding**

### Technical Dashboards:
- **Grafana**: Common tool for technical dashboards
- Dashboards can track key metrics like:
  - **CPU**
  - **GPU** (e.g., for MLOps)
  - **RAM**
  - **Disk Storage**
  - **Kubernetes pods**: Statuses such as Pending, Crashed, or Error

### Business Dashboards:
- **Metabase**: Useful for business metrics, including:
  - Payment processes
  - Customer churn rates
  - Other business KPIs

---

# **Notifications/Alerting**
For alerts, we can use corporate messaging platforms, including:
- **Slack**, **Email**, or **SMS** for notifications
- **Auto conference calls** for critical production alerts

### Integrations:
- **Grafana/Prometheus**: Set up alerts for system overloads (CPU, RAM, disk memory) or when Kubernetes pods fail to respond
- **Metabase**: Integration for business-related alerts (e.g., payment issues or KPI changes)
