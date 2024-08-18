from dnslib import DNSRecord, DNSHeader, RR, QTYPE, SRV
from dnslib.server import DNSServer

# Статические записи для DNS
dns_records = {
    "_feed._udp.catdomain.local.": SRV(0, 0, 12345, "localhost."),
    "_pet._tcp.catdomain.local.": SRV(0, 0, 54321, "localhost.")
}

class CustomDNSResolver:
    def resolve(self, request, handler):
        reply = request.reply()
        qname = str(request.q.qname)
        qtype = QTYPE[request.q.qtype]
        # print("="*10)
        # print(f'|||{qname}|||', qtype)
        # print("="*10)
        # print(qname in dns_records)
        # print(qtype == 'SRV')
        # print(dns_records)
        # for i, c in enumerate(qname):
        #     if c != dns_records.keys()[0][i]:
        #         print(i, c, dns_records.keys()[0][i])

        if qname in dns_records and qtype == 'SRV':
            reply.add_answer(RR(qname, QTYPE.SRV, rdata=dns_records[qname]))
            print(f"Resolved {qname} -> {dns_records[qname]}")
        else:
            print(f"No SRV record found for {qname}")
        
        return reply

if __name__ == "__main__":
    resolver = CustomDNSResolver()
    server = DNSServer(resolver, port=53, address="0.0.0.0", tcp=True)
    print("Starting DNS server...")
    server.start_thread()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            break
