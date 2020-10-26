from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
from diagrams.aws.network import CloudFront
from diagrams.aws.security import WAF
from diagrams.custom import Node

graph_attr = {
    "fontsize": "45",
    "dpi": "300",
    "labelloc": "t"
}

with Diagram("Environment with WAF", graph_attr=graph_attr):

    internet = Node("internet", image="cloud.png", color="white")

    with Cluster("aws account"):
        edge_waf = WAF("edge waf")
        cloudfront = CloudFront("cloudfront cdn")

        with Cluster("vpc"):
            web_lb = ELB("web tier lb")
            with Cluster("web autoscaling group"):
                web_tier = [EC2("web1 instance"), EC2("web2 instance"), EC2("web3 instance")]

            app_waf = WAF("app waf")
            app_lb = ELB("app tier lb")
            with Cluster("app autoscaling group"):
                app_tier = [EC2("app1 instance"), EC2("app2 instance"), EC2("app3 instance")]

            rds = RDS("sql rds cluster")


    internet >> edge_waf >> cloudfront >> web_lb >> web_tier >> app_waf >> app_lb >> app_tier >> Edge(reverse=True) << rds
