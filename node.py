class Node():
    """ Object representing an EC2 node """

    # list of job names
    jobs = []

    def __init__(self, name, id, image_id, key_name, zone,
            instance_type, dns_name, private_dns_name,
            ip_address, private_ip_address, user, job=None):

        self.name = name
        self.id = id
        self.image_id = image_id
        self.key_name = key_name
        self.zone = zone
        self.instance_type = instance_type
        self.dns_name = dns_name
        self.private_dns_name = private_dns_name
        self.ip_address = ip_address
        self.private_ip_address = private_ip_address
        self.user = user
        if job:
            self.add_job(job)

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'image_id': self.image_id,
            'key_name': self.key_name,
            'zone': self.zone,
            'instance_type': self.instance_type,
            'dns_name': self.dns_name,
            'private_dns_name': self.private_dns_name,
            'ip_address': self.ip_address,
            'private_ip_address': self.private_ip_address,
            'user': self.user,
            'jobs': self.jobs
        }            


    def add_job(self, job):
        if job not in self.jobs:
            self.jobs.append(job)
