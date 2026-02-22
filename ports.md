# TCP/UDP Port Numbers

| Port | TCP | UDP | SCTP | DCCP | Description |
|-----:|:---:|:---:|:----:|:----:|:------------|
| 0 | Reserved | Reserved |  |  | In programming APIs (not in communication between hosts), requests a system-allocated (dynamic) port |
| 1 | Yes | Assigned |  |  | TCP Port Service Multiplexer (TCPMUX). Historic. Both TCP and UDP have been assigned to TCPMUX by IANA, |
| 2-3 | Reserved | Reserved |  |  | De-assigned on 2025-02-13, previously compressnet |
| 5 | Assigned | Assigned |  |  | Remote Job Entry was historically using socket 5 in its old socket form, while MIB PIM has identified it as TCP/5 and IANA has assigned both TCP and UDP 5 to it. |
| 7 | Yes | Yes |  |  | Echo Protocol |
| 9 | Yes | Yes | Yes | Assigned | Discard Protocol |
| 9 |  | Unofficial |  |  | Wake-on-LAN |
| 11 | Yes | Yes |  |  | Active Users (systat service) |
| 13 | Yes | Yes |  |  | Daytime Protocol |
| 15 | Unofficial |  |  |  | Previously netstat service |
| 17 | Yes | Yes |  |  | Quote of the Day (QOTD) |
| 18 | Yes | Yes |  |  | Message Send Protocol |
| 19 | Yes | Yes |  |  | Character Generator Protocol (CHARGEN) |
| 20 | Yes | Assigned | Yes |  | File Transfer Protocol (FTP) data transfer |
| 21 | Yes | Assigned | Yes |  | File Transfer Protocol (FTP) control (command) |
| 22 | Yes | Assigned | Yes |  | Secure Shell (SSH), secure logins, file transfers (scp, sftp) and port forwarding |
| 23 | Yes | Assigned |  |  | Telnet protocol—unencrypted text communications |
| 24 | Yes | Assigned |  |  | "any private mail system", often used for LMTP. |
| 25 | Yes | Assigned |  |  | Simple Mail Transfer Protocol (SMTP), used for email routing between mail servers |
| 27 | Assigned | Assigned |  |  | nsw-fe (NSW User System FE) |
| 28 | Unofficial |  |  |  | Palo Alto Networks' Panorama High Availability (HA) sync encrypted port. |
| 29 | Assigned | Assigned |  |  | msg-icp (MSG ICP) |
| 31 | Assigned | Assigned |  |  | msg-auth (MSG Authentication) |
| 33 | Assigned | Assigned |  |  | dsp (Display Support Protocol) |
| 37 | Yes | Yes |  |  | Time Protocol |
| 38 | Assigned | Assigned |  |  | rap (Route Access Protocol) |
| 39 | Assigned | Assigned |  |  | rlp (Resource Location Protocol) |
| 41 | Assigned | Assigned |  |  | graphics (Graphics) |
| 42 | Assigned | Yes |  |  | Host Name Server Protocol |
| 43 | Yes | Assigned |  |  | WHOIS protocol |
| 44 | Assigned | Assigned |  |  | mpm-flags (MPM FLAGS Protocol) |
| 45 | Assigned | Assigned |  |  | mpm (Message Processing Module [recv]) |
| 46 | Assigned | Assigned |  |  | mpm-snd (MPM [default send]) |
| 47 | Reserved | Reserved |  |  | Removed by IANA on 2017-05-18. |
| 48 | Assigned | Assigned |  |  | auditd (Digital Audit Daemon) |
| 49 | Yes | Yes |  |  | TACACS Login Host protocol. TACACS+, still in draft which is an improved but distinct version of TACACS, only uses TCP 49. |
| 50 | Assigned | Assigned |  |  | re-mail-ck (Remote Mail Checking Protocol) |
| 51 | Reserved | Reserved |  |  | Historically used for Interface Message Processor logical address management, entry has been removed by IANA on 2013-05-25 |
| 52 | Assigned | Assigned |  |  | Xerox Network Systems (XNS) Time Protocol. Despite this port being assigned by IANA, the service is meant to work on SPP (ancestor of IPX/SPX), instead of TCP/IP. |
| 53 | Yes | Yes |  |  | Domain Name System (DNS) |
| 54 | Assigned | Assigned |  |  | Xerox Network Systems (XNS) Clearinghouse (Name Server). Despite this port being assigned by IANA, the service is meant to work on SPP (ancestor of IPX/SPX), instead of TCP/IP. |
| 55 | Assigned | Assigned |  |  | isi-gl (ISI Graphics Language) |
| 56 | Assigned | Assigned |  |  | Xerox Network Systems (XNS) Authentication Protocol. Despite this port being assigned by IANA, the service is meant to work on SPP (ancestor of IPX/SPX), instead of TCP/IP. |
| 58 | Assigned | Assigned |  |  | Xerox Network Systems (XNS) Mail. Despite this port being assigned by IANA, the service is meant to work on SPP (ancestor of IPX/SPX), instead of TCP/IP. |
| 61 | Reserved | Reserved |  |  | Historically assigned to the NIFTP-Based Mail protocol, but was never documented in the related IEN. The port number entry was removed from IANA's registry on 2017-05-18. |
| 62 | Assigned | Assigned |  |  | acas (ACA Services) |
| 63 | Assigned | Assigned |  |  | whoispp (whois++) |
| 64 | Assigned | Assigned |  |  | covia (Communications Integrator (CI)) |
| 65 | Assigned | Assigned |  |  | tacacs-ds (TACACS-Database Service) |
| 66 | Assigned | Assigned |  |  | sql-net (Oracle SQL*NET) |
| 67 | Assigned | Yes |  |  | Bootstrap Protocol (BOOTP) server; also used by Dynamic Host Configuration Protocol (DHCP) |
| 68 | Assigned | Yes |  |  | Bootstrap Protocol (BOOTP) client; also used by Dynamic Host Configuration Protocol (DHCP) |
| 69 | Assigned | Yes |  |  | Trivial File Transfer Protocol (TFTP) |
| 70 | Yes | Assigned |  |  | Gopher protocol |
| 71-74 | Yes | Yes |  |  | NETRJS protocol |
| 76 | Assigned | Assigned |  |  | deos (Distributed External Object Store) |
| 78 | Assigned | Assigned |  |  | vettcp (vettcp) |
| 79 | Yes | Assigned |  |  | Finger protocol |
| 80 | Yes | Yes | Yes |  | Hypertext Transfer Protocol (HTTP) uses TCP in versions 1.x and 2. HTTP/3 uses QUIC, a transport protocol on top of UDP. |
| 81 | Unofficial |  |  |  | TorPark onion routing |
| 82 | Assigned | Assigned |  |  | xfer (XFER Utility) |
| 82 | Unofficial |  |  |  | TorPark control |
| 83 | Assigned | Assigned |  |  | mit-ml-dev (MIT ML Device) |
| 84 | Assigned | Assigned |  |  | ctf (Common Trace Facility) |
| 85 | Assigned | Assigned |  |  | mit-ml-dev (MIT ML Device) |
| 86 | Assigned | Assigned |  |  | mfcobol (Micro Focus Cobol) |
| 88 | Yes | Yes |  |  | Kerberos authentication system |
| 89 | Assigned | Assigned |  |  | su-mit-tg (SU/MIT Telnet Gateway) |
| 90 | Assigned | Assigned |  |  | dnsix (DNSIX Security Attribute Token Map) |
| 90 | Unofficial | Unofficial |  |  | PointCast (dotcom) |
| 91 | Assigned | Assigned |  |  | mit-dov (MIT Dover Spooler) |
| 92 | Assigned | Assigned |  |  | npp (Network Printing Protocol) |
| 93 | Assigned | Assigned |  |  | dcp (Device Control Protocol) |
| 94 | Assigned | Assigned |  |  | objcall (Tivoli Object Dispatcher) |
| 95 | Yes | Assigned |  |  | SUPDUP, terminal-independent remote login |
| 96 | Assigned | Assigned |  |  | dixie (DIXIE Protocol Specification) |
| 97 | Assigned | Assigned |  |  | swift-rvf (Swift Remote Virtual File Protocol) |
| 98 | Assigned | Assigned |  |  | tacnews (TAC News) |
| 99 | Assigned | Assigned |  |  | metagram (Metagram Relay) |
| 101 | Yes | Assigned |  |  | NIC host name |
| 102 | Yes | Assigned |  |  | ISO Transport Service Access Point (TSAP) Class 0 protocol; |
| 104 | Yes | Yes |  |  | Digital Imaging and Communications in Medicine (DICOM; also port 11112) |
| 105 | Yes | Yes |  |  | CCSO Nameserver |
| 106 | Unofficial |  |  |  | macOS Server, (macOS) password server |
| 107 | Yes | Yes |  |  | Remote User Telnet Service (RTelnet) |
| 108 | Yes | Yes |  |  | IBM Systems Network Architecture (SNA) gateway access server |
| 109 | Yes | Assigned |  |  | Post Office Protocol, version 2 (POP2) |
| 110 | Yes | Assigned |  |  | Post Office Protocol, version 3 (POP3) |
| 111 | Yes | Yes |  |  | Open Network Computing Remote Procedure Call (ONC RPC, sometimes referred to as Sun RPC) |
| 112 | Yes | Yes |  |  | McIDAS Data Transmission Protocol |
| 113 | Yes |  |  |  | Ident, authentication service/identification protocol, used by IRC servers to identify users |
| 113 | Yes | Assigned |  |  | Authentication Service (auth), the predecessor to identification protocol. Used to determine a user's identity of a particular TCP connection. |
| 115 | Yes | Assigned |  |  | Simple File Transfer Protocol |
| 117 | Yes | Yes |  |  | UUCP Mapping Project (path service) |
| 118 | Yes | Yes |  |  | Structured Query Language (SQL) Services |
| 119 | Yes | Assigned |  |  | Network News Transfer Protocol (NNTP), |
| 123 | Assigned | Yes |  |  | Network Time Protocol (NTP), used for time synchronization |
| 126 | Yes | Yes |  |  | Formerly Unisys Unitary Login, renamed by Unisys to NXEdit. Used by Unisys Programmer's Workbench for Clearpath MCP, an IDE for Unisys MCP software development |
| 135 | Yes | Yes |  |  | DCE endpoint resolution |
| 135 | Yes | Yes |  |  | Microsoft EPMAP (End Point Mapper), also known as DCE/RPC Locator service, used to remotely manage services including DHCP server, DNS server and WINS. Also used by DCOM |
| 137 | Yes | Yes |  |  | NetBIOS Name Service, used for name registration and resolution |
| 138 | Assigned | Yes |  |  | NetBIOS Datagram Service |
| 139 | Yes | Assigned |  |  | NetBIOS Session Service |
| 143 | Yes | Assigned |  |  | Internet Message Access Protocol (IMAP), |
| 151 | Assigned | Assigned |  |  | HEMS |
| 152 | Yes | Yes |  |  | Background File Transfer Program (BFTP) |
| 153 | Yes | Yes |  |  | Simple Gateway Monitoring Protocol (SGMP), a protocol for remote inspection and alteration of gateway management information |
| 156 | Yes | Yes |  |  | Structured Query Language (SQL) Service |
| 158 | Yes | Yes |  |  | Distributed Mail System Protocol (DMSP, sometimes referred to as Pcmail) |
| 161 | Assigned | Yes |  |  | Simple Network Management Protocol (SNMP) |
| 162 | Yes | Yes |  |  | Simple Network Management Protocol Trap (SNMPTRAP) |
| 165 | Assigned | Assigned |  |  | Xerox |
| 169 | Assigned | Assigned |  |  | SEND |
| 170 | Yes | Yes |  |  | Network PostScript print server |
| 175 | Yes | Yes |  |  | VMNET service using NJE |
| 177 | Yes | Yes |  |  | X Display Manager Control Protocol (XDMCP), used for remote logins to an X Display Manager server |
| 179 | Yes | Assigned | Yes |  | Border Gateway Protocol (BGP), used to exchange routing and reachability information among autonomous systems (AS) on the Internet |
| 180 | Assigned | Assigned |  |  | ris |
| 194 | Yes | Yes |  |  | Internet Relay Chat (IRC) |
| 199 | Yes | Yes |  |  | SNMP Unix Multiplexer (SMUX) |
| 201 | Yes | Yes |  |  | AppleTalk Routing Maintenance |
| 209 | Yes | Assigned |  |  | Quick Mail Transfer Protocol |
| 210 | Yes | Yes |  |  | ANSI Z39.50 |
| 213 | Yes | Yes |  |  | Internetwork Packet Exchange (IPX) |
| 218 | Yes | Yes |  |  | Message posting protocol (MPP) |
| 220 | Yes | Yes |  |  | Internet Message Access Protocol (IMAP), version 3 |
| 225-241 | Reserved | Reserved |  |  |  |
| 249-255 | Reserved | Reserved |  |  |  |
| 259 | Yes | Yes |  |  | Efficient Short Remote Operations (ESRO) |
| 262 | Yes | Yes |  |  | Arcisdms |
| 264 | Yes | Yes |  |  | Border Gateway Multicast Protocol (BGMP) |
| 280 | Yes | Yes |  |  | http-mgmt |
| 300 | Unofficial |  |  |  | ThinLinc Web Access, Spartan protocol |
| 308 | Yes |  |  |  | Novastor Online Backup |
| 311 | Yes | Assigned |  |  | macOS Server Admin (officially AppleShare IP Web administration) |
| 312 | Unofficial |  |  |  | macOS Xsan administration |
| 318 | Yes | Yes |  |  | PKIX Time Stamp Protocol (TSP) |
| 319 |  | Yes |  |  | Precision Time Protocol (PTP) event messages |
| 320 |  | Yes |  |  | Precision Time Protocol (PTP) general messages |
| 323 | Yes |  |  |  | Resource Public Key Infrastructure |
| 350 | Yes | Yes |  |  | Mapping of Airline Traffic over Internet Protocol (MATIP) type A |
| 351 | Yes | Yes |  |  | MATIP type B |
| 356 | Yes | Yes |  |  | cloanto-net-1 (used by Cloanto Amiga Explorer and VMs) |
| 366 | Yes | Yes |  |  | On-Demand Mail Relay (ODMR) |
| 369 | Yes | Yes |  |  | Rpc2portmap |
| 370 | Yes | Yes |  |  | codaauth2, Coda authentication server |
| 370 | Yes |  |  |  | securecast1, outgoing packets to NAI's SecureCast servers |
| 371 | Yes | Yes |  |  | ClearCase albd |
| 376 | Yes | Yes |  |  | Amiga Envoy Network Inquiry Protocol |
| 383 | Yes | Yes |  |  | HP data alarm manager |
| 384 | Yes | Yes |  |  | A Remote Network Server System |
| 387 | Yes | Yes |  |  | AURP (AppleTalk Update-based Routing Protocol) |
| 388 | Yes | Assigned |  |  | Unidata LDM near real-time data distribution protocol |
| 389 | Yes | Assigned |  |  | Lightweight Directory Access Protocol (LDAP) |
| 399 | Yes | Yes |  |  | Digital Equipment Corporation DECnet+ (Phase V) over TCP/IP (RFC1859) |
| 401 | Yes | Yes |  |  | Uninterruptible power supply (UPS) |
| 427 | Yes | Yes |  |  | Service Location Protocol (SLP) |
| 433 | Yes | Yes |  |  | NNTP, part of Network News Transfer Protocol |
| 443 | Yes | Yes | Yes |  | Hypertext Transfer Protocol Secure (HTTPS) uses TCP in versions 1.x and 2. HTTP/3 uses QUIC, a transport protocol on top of UDP. |
| 444 | Yes | Yes |  |  | Simple Network Paging Protocol (SNPP), RFC 1568 |
| 445 | Yes | Yes |  |  | Microsoft-DS (Directory Services) Active Directory, Windows shares |
| 445 | Yes | Assigned |  |  | Microsoft-DS (Directory Services) SMB file sharing |
| 464 | Yes | Yes |  |  | Kpasswd: Kerberos Change/Set password |
| 475 | Yes | Yes |  |  | tcpnethaspsrv, Aladdin Knowledge Systems Hasp services |
| 476-490 | Unofficial | Unofficial |  |  | Centro Software ERP ports |
| 491 | Unofficial |  |  |  | GO-Global remote access and application publishing software |
| 497 | Yes | Yes |  |  | Retrospect |
| 500 | Assigned | Yes |  |  | Internet Security Association and Key Management Protocol (ISAKMP) / Internet Key Exchange (IKE) |
| 502 | Yes | Yes |  |  | Modbus Protocol |
| 504 | Yes | Yes |  |  | Citadel, multiservice protocol for dedicated clients for the Citadel groupware system |
| 510 | Yes | Yes |  |  | FirstClass Protocol (FCP), used by FirstClass client/server groupware system |
| 512 | Yes |  |  |  | Rexec, Remote Process Execution |
| 512 | Yes |  |  |  | comsat, together with biff |
| 513 | Yes |  |  |  | rlogin |
| 513 | Yes |  |  |  | Who |
| 514 | Unofficial |  |  |  | Remote Shell, used to execute non-interactive commands on a remote system (Remote Shell, rsh, remsh) |
| 514 |  | Yes |  |  | Syslog, used for system logging |
| 515 | Yes | Assigned |  |  | Line Printer Daemon (LPD), print service |
| 517 |  | Yes |  |  | Talk |
| 518 |  | Yes |  |  | NTalk |
| 520 | Yes |  |  |  | efs, extended file name server |
| 520 | Yes |  |  |  | Routing Information Protocol (RIP) |
| 521 |  | Yes |  |  | Routing Information Protocol Next Generation (RIPng) |
| 524 | Yes | Yes |  |  | NetWare Core Protocol (NCP) is used for a variety things such as access to primary NetWare server resources, Time Synchronization, etc. |
| 525 |  | Yes |  |  | Timed, Timeserver |
| 530 | Yes | Yes |  |  | Remote procedure call (RPC) |
| 532 | Yes | Assigned |  |  | netnews |
| 533 |  | Yes |  |  | netwall, for emergency broadcasts |
| 540 | Yes |  |  |  | Unix-to-Unix Copy Protocol (UUCP) |
| 542 | Yes | Yes |  |  | commerce (Commerce Applications) |
| 543 | Yes |  |  |  | klogin, Kerberos login |
| 544 | Yes |  |  |  | kshell, Kerberos Remote shell |
| 546 | Yes | Yes |  |  | DHCPv6 client |
| 547 | Yes | Yes |  |  | DHCPv6 server |
| 548 | Yes | Assigned |  |  | Apple Filing Protocol (AFP) over TCP |
| 550 | Yes | Yes |  |  | new-rwho, new-who |
| 554 | Yes | Yes |  |  | Real Time Streaming Protocol (RTSP) |
| 556 | Yes |  |  |  | Remotefs, RFS, rfs_server |
| 560 |  | Yes |  |  | rmonitor, Remote Monitor |
| 561 |  | Yes |  |  | monitor |
| 563 | Yes | Yes |  |  | NNTP over TLS/SSL (NNTPS) |
| 564 | Unofficial |  |  |  | 9P (Plan 9) |
| 585 |  |  |  |  | Previously assigned for use of Internet Message Access Protocol over TLS/SSL (IMAPS), now deregistered in favour of port 993. |
| 587 | Yes | Assigned |  |  | Email Message Submission (No longer preferred; see port 465.) |
| 591 | Yes |  |  |  | FileMaker 6.0 (and later) Web Sharing (HTTP Alternate, also see port 80) |
| 593 | Yes | Yes |  |  | HTTP RPC Ep Map, Remote procedure call over Hypertext Transfer Protocol, often used by Distributed Component Object Model services and Microsoft Exchange Server |
| 601 | Yes |  |  |  | Reliable Syslog Service — used for system logging |
| 604 | Yes |  |  |  | TUNNEL profile, a protocol for BEEP peers to form an application layer tunnel |
| 623 |  | Yes |  |  | ASF Remote Management and Control Protocol (ASF-RMCP) & IPMI Remote Management Protocol |
| 625 | Unofficial |  |  |  | Open Directory Proxy (ODProxy) |
| 631 | Yes | Yes |  |  | Internet Printing Protocol (IPP) |
| 631 | Unofficial | Unofficial |  |  | Common Unix Printing System (CUPS) administration console (extension to IPP) |
| 635 | Yes | Yes |  |  | RLZ DBase |
| 636 | Yes | Assigned |  |  | Lightweight Directory Access Protocol over TLS/SSL (LDAPS) |
| 639 | Yes | Yes |  |  | Multicast Source Discovery Protocol, MSDP |
| 641 | Yes | Yes |  |  | SupportSoft Nexus Remote Command (control/listening), a proxy gateway connecting remote control traffic |
| 643 | Yes | Yes |  |  | SANity |
| 646 | Yes | Yes |  |  | Label Distribution Protocol (LDP), a routing protocol used in MPLS networks |
| 647 | Yes |  |  |  | DHCP Failover protocol |
| 648 | Yes |  |  |  | Registry Registrar Protocol (RRP) |
| 651 | Yes | Yes |  |  | IEEE-MMS |
| 653 | Yes | Yes |  |  | SupportSoft Nexus Remote Command (data), a proxy gateway connecting remote control traffic |
| 654 | Yes |  |  |  | Media Management System (MMS) Media Management Protocol (MMP) |
| 655 | Yes | Yes |  |  | Tinc VPN daemon |
| 657 | Yes | Yes |  |  | IBM RMC (Remote monitoring and Control) protocol, used by System p5 AIX Integrated Virtualization Manager (IVM) and Hardware Management Console to connect managed logical partitions (LPAR) to enable dynamic partition reconfiguration |
| 660 | Yes | Assigned |  |  | macOS Server administration, version 10.4 and earlier |
| 662 | Yes | Yes |  |  | NFS v3 Statd port |
| 666 | Yes | Yes |  |  | Doom, the first online first-person shooter |
| 666 | Unofficial |  |  |  | airserv-ng, aircrack-ng's server for remote-controlling wireless devices |
| 674 | Yes |  |  |  | Application Configuration Access Protocol (ACAP) |
| 684 | Yes | Yes |  |  | CORBA IIOP SSL |
| 688 | Yes | Yes |  |  | REALM-RUSD (ApplianceWare Server Appliance Management Protocol) |
| 690 | Yes | Yes |  |  | Velneo Application Transfer Protocol (VATP) |
| 691 | Yes |  |  |  | MS Exchange Routing |
| 694 | Yes | Yes |  |  | Linux-HA high-availability heartbeat |
| 695 | Yes | Assigned |  |  | IEEE Media Management System over SSL (IEEE-MMS-SSL) |
| 698 |  | Yes |  |  | Optimized Link State Routing (OLSR) |
| 700 | Yes |  |  |  | Extensible Provisioning Protocol (EPP), a protocol for communication between domain name registries and registrars (RFC 5734) |
| 701 | Yes |  |  |  | Link Management Protocol (LMP), a protocol that runs between a pair of nodes and is used to manage traffic engineering (TE) links |
| 702 | Yes |  |  |  | IRIS (Internet Registry Information Service) over BEEP (Blocks Extensible Exchange Protocol) (RFC 3983) |
| 706 | Yes |  |  |  | Secure Internet Live Conferencing (SILC) |
| 711 | Yes |  |  |  | Cisco Tag Distribution Protocol—being replaced by the MPLS Label Distribution Protocol |
| 712 | Yes |  |  |  | Topology Broadcast based on Reverse-Path Forwarding routing protocol (TBRPF; RFC 3684) |
| 749 | Yes | Yes |  |  | Kerberos administration |
| 750 |  | Yes |  |  | kerberos-iv, Kerberos version IV |
| 751 | Unofficial | Unofficial |  |  | kerberos_master, Kerberos authentication |
| 752 |  | Unofficial |  |  | passwd_server, Kerberos password (kpasswd) server |
| 753 | Yes | Yes |  |  | Reverse Routing Header (RRH) |
| 753 | Unofficial |  |  |  | userreg_server, Kerberos userreg server |
| 754 | Yes | Yes |  |  | tell send |
| 754 | Unofficial |  |  |  | krb5_prop, Kerberos v5 slave propagation |
| 760 | Unofficial | Unofficial |  |  | krbupdate [kreg], Kerberos registration |
| 777 | Unofficial | Unofficial |  |  | machine socket eXtension [msx] protocol |
| 782 | Unofficial |  |  |  | Conserver serial-console management server |
| 783 | Unofficial |  |  |  | SpamAssassin spamd daemon |
| 800 | Yes | Yes |  |  | mdbs-daemon |
| 802 | Yes | Yes |  |  | MODBUS/TCP Security |
| 808 | Unofficial |  |  |  | Microsoft Net.TCP Port Sharing Service |
| 829 | Yes | Assigned |  |  | Certificate Management Protocol |
| 830 | Yes | Yes |  |  | NETCONF over SSH |
| 831 | Yes | Yes |  |  | NETCONF over BEEP |
| 832 | Yes | Yes |  |  | NETCONF for SOAP over HTTPS |
| 833 | Yes | Yes |  |  | NETCONF for SOAP over BEEP |
| 843 | Unofficial |  |  |  | Adobe Flash |
| 847 | Yes |  |  |  | DHCP Failover protocol |
| 848 | Yes | Yes |  |  | Group Domain Of Interpretation (GDOI) protocol |
| 853 | Yes |  |  |  | DNS over TLS (RFC 7858) |
| 853 | Yes |  |  |  | DNS over QUIC or DNS over DTLS |
| 860 | Yes |  |  |  | iSCSI (RFC 3720) |
| 861 | Yes | Yes |  |  | OWAMP control (RFC 4656) |
| 862 | Yes | Yes |  |  | TWAMP control (RFC 5357) |
| 873 | Yes |  |  |  | rsync file synchronization protocol |
| 888 | Unofficial |  |  |  | cddbp, CD DataBase (CDDB) protocol (CDDBP) |
| 888 | Unofficial |  |  |  | IBM Endpoint Manager Remote Control |
| 892 | Yes | Yes |  |  | NFS v3 Mountd port |
| 897 | Unofficial | Unofficial |  |  | Brocade SMI-S RPC |
| 898 | Unofficial | Unofficial |  |  | Brocade SMI-S RPC SSL |
| 902 | Unofficial | Unofficial |  |  | VMware ESXi |
| 903 | Unofficial |  |  |  | VMware ESXi |
| 953 | Yes | Reserved |  |  | BIND remote name daemon control (RNDC) |
| 981 | Unofficial |  |  |  | Remote HTTPS management for firewall devices running embedded Check Point VPN-1 software |
| 987 | Unofficial |  |  |  | Sony PlayStation Wake On Lan |
| 987 | Unofficial |  |  |  | Microsoft Remote Web Workplace, a feature of Windows Small Business Server |
| 988 | Unofficial |  |  |  | Lustre (file system) Protocol (data). |
| 989 | Yes | Yes |  |  | FTPS Protocol (data), FTP over TLS/SSL |
| 990 | Yes | Yes |  |  | FTPS Protocol (control), FTP over TLS/SSL |
| 991 | Yes | Yes |  |  | Netnews Administration System (NAS) |
| 992 | Yes | Yes |  |  | Telnet protocol over TLS/SSL |
| 993 | Yes | Assigned |  |  | Internet Message Access Protocol over TLS/SSL (IMAPS) |
| 994 | Reserved | Reserved |  |  | Previously assigned to Internet Relay Chat over TLS/SSL (IRCS), but was not used in common practice. |
| 995 | Yes | Yes |  |  | Post Office Protocol 3 over TLS/SSL (POP3S) |
| 1010 | Unofficial |  |  |  | ThinLinc web-based administration interface |
| 1011-1020 | Reserved | Reserved |  |  |  |
| 1023 | Reserved | Reserved |  |  |  |
| 1023 |  |  |  |  | } |
| 1024 | Reserved | Reserved |  |  | Reserved |
| 1025 | Assigned | Assigned |  |  | network blackjack |
| 1027 | Reserved |  |  |  | Reserved |
| 1027 | Yes |  |  |  | Native IPv6 behind IPv4-to-IPv4 NAT Customer Premises Equipment (6a44) |
| 1029 | Unofficial | Unofficial |  |  | Microsoft DCOM services |
| 1058 | Yes | Yes |  |  | nim, IBM AIX Network Installation Manager (NIM) |
| 1059 | Yes | Yes |  |  | nimreg, IBM AIX Network Installation Manager (NIM) |
| 1080 | Yes | Yes |  |  | SOCKS proxy |
| 1085 | Yes | Yes |  |  | WebObjects |
| 1098 | Yes | Yes |  |  | rmiactivation, Java remote method invocation (RMI) activation |
| 1099 | Yes | Assigned |  |  | rmiregistry, Java remote method invocation (RMI) registry |
| 1100 |  | Unofficial |  |  | SaltoSystems - Handshake for IP-Components |
| 1112 | Unofficial |  |  |  | ESET virus updates |
| 1113 | Assigned | Yes |  |  | Licklider Transmission Protocol (LTP) delay tolerant networking protocol |
| 1119 | Yes | Yes |  |  | Battle.net chat/game protocol, used by Blizzard's games |
| 1144 | Yes | Yes |  |  | fuscript (Fusion Script) used by Blackmagic Design Fusion and DaVinci Resolve |
| 1167 | Yes | Yes | Yes |  | Cisco IP SLA (Service Assurance Agent) |
| 1194 | Yes | Yes |  |  | OpenVPN |
| 1198 | Yes | Yes |  |  | The cajo project Free dynamic transparent distributed computing in Java |
| 1212 | Unofficial | Unofficial |  |  | Equalsocial Fediverse protocol |
| 1214 | Yes | Yes |  |  | Kazaa |
| 1220 | Yes | Assigned |  |  | QuickTime Streaming Server administration |
| 1234 | Yes | Yes |  |  | Infoseek search agent |
| 1234 | Unofficial |  |  |  | VLC media player default port for UDP/RTP stream |
| 1241 | Unofficial | Unofficial |  |  | Nessus Security Scanner |
| 1270 | Yes | Yes |  |  | Microsoft System Center Operations Manager (SCOM) (formerly Microsoft Operations Manager (MOM)) agent |
| 1293 | Yes | Yes |  |  | Internet Protocol Security (IPSec) |
| 1311 | Yes | Yes |  |  | Windows <code>RxMon.exe</code> |
| 1311 | Unofficial |  |  |  | Dell OpenManage HTTPS |
| 1314 | Unofficial | Unofficial |  |  | Festival Speech Synthesis System server |
| 1319 | Yes | Yes |  |  | AMX ICSP (Protocol for communications with AMX control systems devices) |
| 1337 | Yes | Yes |  |  | Men&Mice DNS |
| 1337 | Unofficial |  |  |  | Strapi |
| 1337 | Unofficial |  |  |  | Razer Chroma SDK Server |
| 1337 | Unofficial |  |  |  | Sails.js default port |
| 1341 | Yes | Yes |  |  | Qubes (Manufacturing Execution System) |
| 1344 | Yes | Yes |  |  | Internet Content Adaptation Protocol |
| 1352 | Yes | Yes |  |  | HCL Notes / Domino (RPC) protocol |
| 1360 | Yes | Yes |  |  | Mimer SQL |
| 1414 | Yes | Yes |  |  | IBM WebSphere MQ (formerly known as MQSeries) |
| 1417 | Yes | Yes |  |  | Timbuktu Service 1 Port |
| 1418 | Yes | Yes |  |  | Timbuktu Service 2 Port |
| 1419 | Yes | Yes |  |  | Timbuktu Service 3 Port |
| 1420 | Yes | Yes |  |  | Timbuktu Service 4 Port |
| 1431 | Yes |  |  |  | Reverse Gossip Transport Protocol (RGTP), used to access a General-purpose Reverse-Ordered Gossip Gathering System (GROGGS) bulletin board, such as that implemented on the Cambridge University's Phoenix system |
| 1433 | Yes | Yes |  |  | Microsoft SQL Server database management system (MSSQL) server |
| 1434 | Yes | Yes |  |  | Microsoft SQL Server database management system (MSSQL) monitor |
| 1476 | Yes | Yes |  |  | WiFi Pineapple Hak5. |
| 1481 | Yes | Yes |  |  | AIRS data interchange. |
| 1492 | Unofficial |  |  |  | Sid Meier's CivNet, a multiplayer remake of the original Sid Meier's Civilization game |
| 1494 | Unofficial | Unofficial |  |  | Citrix Independent Computing Architecture (ICA) |
| 1500 | Unofficial |  |  |  | IBM Tivoli Storage Manager server |
| 1501 | Unofficial |  |  |  | IBM Tivoli Storage Manager client scheduler |
| 1503 | Unofficial | Unofficial |  |  | Windows Live Messenger (Whiteboard and Application Sharing) |
| 1512 | Yes | Yes |  |  | Microsoft's Windows Internet Name Service (WINS) |
| 1513 | Unofficial | Unofficial |  |  | Garena game client |
| 1521 | Yes | Yes |  |  | nCUBE License Manager |
| 1521 | Unofficial |  |  |  | Oracle database default listener, in future releases official port 2483 (TCP/IP) and 2484 (TCP/IP with SSL) |
| 1524 | Yes | Yes |  |  | ingreslock, ingres |
| 1527 | Yes | Yes |  |  | Oracle Net Services, formerly known as SQL*Net |
| 1527 | Unofficial |  |  |  | Apache Derby Network Server |
| 1533 | Yes | Yes |  |  | IBM Sametime Virtual Places Chat |
| 1534 |  | Unofficial |  |  | Eclipse Target Communication Framework |
| 1540 | Unofficial | Unofficial |  |  | 1C:Enterprise server agent (ragent) |
| 1541 | Unofficial | Unofficial |  |  | 1C:Enterprise master cluster manager (rmngr) |
| 1542 | Unofficial | Unofficial |  |  | 1C:Enterprise configuration repository server |
| 1545 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster administration server (RAS) |
| 1547 | Yes | Yes |  |  | Laplink |
| 1550 | Unofficial | Unofficial |  |  | 1C:Enterprise debug server |
| 1550 | Unofficial |  |  |  | Gadu-Gadu (direct client-to-client) |
| 1560-1580 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1581 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1581 | Yes | Yes |  |  | MIL STD 2045-47001 VMF |
| 1581 | Unofficial |  |  |  | IBM Tivoli Storage Manager web client |
| 1582 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1582 | Unofficial |  |  |  | IBM Tivoli Storage Manager server web interface |
| 1583 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1583 | Unofficial |  |  |  | IBM Tivoli Storage Manager server web interface |
| 1583 | Unofficial | Unofficial |  |  | Pervasive PSQL |
| 1584-1588 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1589 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1589 | Yes | Yes |  |  | Cisco VLAN Query Protocol (VQP) |
| 1590 | Unofficial | Unofficial |  |  | 1C:Enterprise cluster working processes |
| 1604 | Unofficial | Unofficial |  |  | DarkComet remote administration tool (RAT) |
| 1626-1627 | Unofficial |  |  |  | iSketch |
| 1628 | Yes | Yes |  |  | LonTalk normal |
| 1629 | Yes | Yes |  |  | LonTalk urgent |
| 1645 |  | Unofficial |  |  | Early deployment of RADIUS before RFC standardization was done using UDP port number 1645. Enabled for compatibility reasons by default on Cisco and Juniper Networks RADIUS servers. Official port is 1812. TCP port 1645 <span style="text-transform: uppercase;">must not</span> be used for RADIUS. |
| 1646 |  | Unofficial |  |  | Old <code>radacct</code> port, RADIUS accounting protocol. Enabled for compatibility reasons by default on Cisco and Juniper Networks RADIUS servers. Official port is 1813. TCP port 1646 <span style="text-transform: uppercase;">must not</span> be used for RADIUS. |
| 1666 | Unofficial |  |  |  | Perforce |
| 1677 | Yes | Yes |  |  | Novell GroupWise clients in client/server access mode |
| 1688 | Unofficial |  |  |  | Microsoft Key Management Service (KMS) for Windows Activation |
| 1701 | Yes | Yes |  |  | Layer 2 Forwarding Protocol (L2F) |
| 1701 | Assigned | Yes |  |  | Layer 2 Tunneling Protocol (L2TP) |
| 1707 | Yes | Yes |  |  | Windward Studios games (vdmplay) |
| 1707 | Unofficial |  |  |  | L2TP/IPsec, for establishing an initial connection |
| 1714-1715 | Unofficial | Unofficial |  |  | KDE Connect |
| 1716 | Unofficial | Unofficial |  |  | KDE Connect |
| 1716 |  | Unofficial |  |  | America's Army, a massively multiplayer online game (MMO) |
| 1717-1718 | Unofficial | Unofficial |  |  | KDE Connect |
| 1719 | Unofficial | Unofficial |  |  | KDE Connect |
| 1719 | Yes | Yes |  |  | H.323 registration and alternate communication |
| 1720 | Unofficial | Unofficial |  |  | KDE Connect |
| 1720 | Yes | Yes |  |  | H.323 call signaling |
| 1721-1722 | Unofficial | Unofficial |  |  | KDE Connect |
| 1723 | Unofficial | Unofficial |  |  | KDE Connect |
| 1723 | Yes | Assigned |  |  | Point-to-Point Tunneling Protocol (PPTP) |
| 1724-1754 | Unofficial | Unofficial |  |  | KDE Connect |
| 1755 | Unofficial | Unofficial |  |  | KDE Connect |
| 1755 | Yes | Yes |  |  | Microsoft Media Services (MMS, <code>ms-streaming</code>) |
| 1756-1760 | Unofficial | Unofficial |  |  | KDE Connect |
| 1761 | Unofficial | Unofficial |  |  | KDE Connect |
| 1761 | Unofficial | Unofficial |  |  | Novell ZENworks |
| 1762-1764 | Unofficial | Unofficial |  |  | KDE Connect |
| 1776 | Yes | Yes |  |  | Emergency management information system |
| 1801 | Yes | Yes |  |  | Microsoft Message Queuing |
| 1812 | Yes | Yes |  |  | RADIUS authentication protocol, <code>radius</code> |
| 1813 | Yes | Yes |  |  | RADIUS accounting protocol, <code>radius-acct</code> |
| 1863 | Yes | Yes |  |  | Microsoft Notification Protocol (MSNP), used by the Microsoft Messenger service and a number of instant messaging Messenger clients |
| 1880 | Unofficial | Unofficial |  |  | Node-RED |
| 1883 | Yes | Yes |  |  | MQTT (formerly MQ Telemetry Transport) |
| 1900 | Assigned | Yes |  |  | Simple Service Discovery Protocol (SSDP), discovery of UPnP devices |
| 1935 | Yes | Yes |  |  | Macromedia Flash Communications Server MX, the precursor to Adobe Flash Media Server before Macromedia's acquisition by Adobe on December 3, 2005 |
| 1935 | Unofficial | Unofficial |  |  | Real Time Messaging Protocol (RTMP), primarily used in Adobe Flash |
| 1965 | Unofficial |  |  |  | Gemini, a lightweight, collaboratively designed protocol, striving to fill the gap between Gopher and HTTP |
| 1967 |  | Unofficial |  |  | Cisco IOS IP Service Level Agreements (IP SLAs) Control Protocol |
| 1972 | Yes | Yes |  |  | InterSystems Caché, and InterSystems IRIS versions 2020.3 and later |
| 1985 | Assigned | Yes |  |  | Cisco Hot Standby Router Protocol (HSRP) |
| 1998 | Yes | Yes |  |  | Cisco X.25 over TCP (XOT) service |
| 2000 | Yes | Yes |  |  | Cisco Skinny Client Control Protocol (SCCP) |
| 2001-2009 | Unofficial | Unofficial |  |  | hexss http server (python package) |
| 2010 | Unofficial | Unofficial |  |  | Artemis: Spaceship Bridge Simulator |
| 2019 | Unofficial |  |  |  | Caddy admin API endpoint |
| 2033 | Unofficial | Unofficial |  |  | Civilization IV multiplayer |
| 2049 | Yes | Yes | Yes |  | Network File System (NFS) |
| 2056 | Unofficial | Unofficial |  |  | Civilization IV multiplayer |
| 2080 | Yes | Yes |  |  | Autodesk NLM (FLEXlm) |
| 2082 | Unofficial |  |  |  | cPanel default |
| 2083 | Yes | Yes |  |  | Secure RADIUS Service (radsec) |
| 2083 | Unofficial |  |  |  | cPanel default TLS |
| 2086 | Yes | Yes |  |  | GNUnet |
| 2086 | Unofficial |  |  |  | WebHost Manager default |
| 2087 | Unofficial |  |  |  | WebHost Manager default TLS |
| 2095 | Yes |  |  |  | cPanel default web mail |
| 2096 | Unofficial |  |  |  | cPanel default TLS web mail |
| 2100 | Unofficial |  |  |  | Warzone 2100 multiplayer |
| 2101 | Unofficial |  |  |  | Networked Transport of RTCM via Internet Protocol (NTRIP) |
| 2102 | Yes | Yes |  |  | Zephyr Notification Service server |
| 2103 | Yes | Yes |  |  | Zephyr Notification Service <code>serv-hm</code> connection |
| 2104 | Yes | Yes |  |  | Zephyr Notification Service hostmanager |
| 2123 | Yes | Yes |  |  | GTP control messages (GTP-C) |
| 2142 | Yes | Yes |  |  | TDMoIP (TDM over IP) |
| 2152 | Yes | Yes |  |  | GTP user data messages (GTP-U) |
| 2159 | Yes | Yes |  |  | GDB remote debug port |
| 2181 | Yes | Yes |  |  | EForward-document transport system |
| 2181 | Unofficial |  |  |  | Apache ZooKeeper default client port |
| 2195 | Unofficial |  |  |  | Apple Push Notification Service, binary, gateway. Deprecated March 2021. |
| 2196 | Unofficial |  |  |  | Apple Push Notification Service, binary, feedback. Deprecated March 2021. |
| 2197 | Unofficial |  |  |  | Apple Push Notification Service, HTTP/2, JSON-based API. |
| 2210 | Yes | Yes |  |  | NOAAPORT Broadcast Network |
| 2211 | Yes | Yes |  |  | EMWIN |
| 2221 | Unofficial |  |  |  | ESET anti-virus updates |
| 2222 | Yes | Yes |  |  | EtherNet/IP implicit messaging for IO data |
| 2222 | Unofficial | Unofficial |  |  | DirectAdmin Access |
| 2222 | Yes |  |  |  | ESET Remote administrator |
| 2223-2226 | Yes |  |  |  | ESET Remote administrator |
| 2240 | Yes | Yes |  |  | General Dynamics Remote Encryptor Configuration Information Protocol (RECIPe) |
| 2261 | Yes | Yes |  |  | CoMotion master |
| 2262 | Yes | Yes |  |  | CoMotion backup |
| 2302 | Unofficial |  |  |  | ArmA multiplayer |
| 2302 | Unofficial |  |  |  | Halo: Combat Evolved multiplayer host |
| 2303 | Unofficial |  |  |  | ArmA multiplayer (default port for game +1) |
| 2303 | Unofficial |  |  |  | Halo: Combat Evolved multiplayer listener |
| 2305 |  | Unofficial |  |  | ArmA multiplayer (default port for game +3) |
| 2351 | Unofficial |  |  |  | AIM game LAN network port |
| 2368 | Unofficial |  |  |  | Ghost (blogging platform) |
| 2369 | Unofficial |  |  |  | Default for BMC Control-M/Server Configuration Agent |
| 2370 | Unofficial |  |  |  | Default for BMC Control-M/Server, to allow the Control-M/Enterprise Manager to connect to the Control-M/Server |
| 2372 | Unofficial |  |  |  | Default for K9 Web Protection/parental controls, content filtering agent |
| 2375 | Yes | Reserved |  |  | Docker REST API (plain) |
| 2376 | Yes | Reserved |  |  | Docker REST API (SSL) |
| 2377 | Yes | Reserved |  |  | Docker Swarm cluster management communications |
| 2379 | Yes | Reserved |  |  | CoreOS etcd client communication |
| 2379 | Unofficial |  |  |  | KGS Go Server |
| 2380 | Yes | Reserved |  |  | CoreOS etcd server communication |
| 2389 | Assigned | Assigned |  |  | OpenView Session Mgr |
| 2399 | Yes | Yes |  |  | FileMaker Data Access Layer (ODBC/JDBC) |
| 2401 | Yes | Yes |  |  | CVS version control system password-based server |
| 2404 | Yes | Yes |  |  | IEC 60870-5-104, used to send electric power telecontrol messages between two systems via directly connected data circuits |
| 2424 | Unofficial |  |  |  | OrientDB database listening for binary client connections |
| 2426 | Unofficial | Unofficial |  |  | VMware VeloCloud Multipath Protocol (VCMP) Dynamic Multipath Optimization (DMPO) |
| 2427 | Yes | Yes |  |  | Media Gateway Control Protocol (MGCP) media gateway |
| 2447 | Yes | Yes |  |  | ovwdb—OpenView Network Node Manager (NNM) daemon |
| 2456 | Unofficial | Unofficial |  |  | Valheim |
| 2459 | Yes | Yes |  |  | XRPL |
| 2480 | Unofficial |  |  |  | OrientDB database listening for HTTP client connections |
| 2483 | Yes | Yes |  |  | Oracle database listening for insecure client connections, replaces port 1521 |
| 2484 | Yes | Yes |  |  | Oracle database listening for SSL client connections |
| 2500 | Unofficial | Unofficial |  |  | NetFS communication |
| 2501 |  | Unofficial |  |  | NetFS probe |
| 2535 | Yes | Yes |  |  | Multicast Address Dynamic Client Allocation Protocol (MADCAP). All standard messages are UDP datagrams. |
| 2541 | Yes | Yes |  |  | LonTalk/IP |
| 2546-2548 | Yes | Yes |  |  | EVault data protection services |
| 2593 | Unofficial | Unofficial |  |  | Ultima Online servers |
| 2598 | Unofficial |  |  |  | Citrix Independent Computing Architecture (ICA) with Session Reliability; port 1494 without session reliability |
| 2599 | Unofficial | Unofficial |  |  | Ultima Online servers |
| 2628 | Yes | Yes |  |  | DICT |
| 2638 | Yes | Yes |  |  | SQL Anywhere database server |
| 2710 | Unofficial | Unofficial |  |  | XBT Tracker. UDP tracker extension is considered experimental. |
| 2727 | Yes | Yes |  |  | Media Gateway Control Protocol (MGCP) media gateway controller (call agent) |
| 2759 |  | Unofficial |  |  | SuperTuxKart server |
| 2761 | Yes | Yes |  |  | DICOM over Integrated Secure Communication Layer (ISCL) |
| 2762 | Yes | Yes |  |  | DICOM over TLS |
| 2775 | Yes | Yes |  |  | Short Message Peer-to-Peer (SMPP) |
| 2809 | Yes | Yes |  |  | corbaloc:iiop URL, per the CORBA 3.0.3 specification |
| 2811 | Yes | Yes |  |  | gsi ftp, per the GridFTP specification |
| 2827 | Unofficial |  |  |  | I2P BOB Bridge |
| 2944 | Yes | Yes |  |  | Megaco text H.248 |
| 2945 | Yes | Yes |  |  | Megaco binary (ASN.1) H.248 |
| 2947 | Yes | Yes |  |  | gpsd, GPS daemon |
| 2948-2949 | Yes | Yes |  |  | WAP push Multimedia Messaging Service (MMS) |
| 2967 | Yes | Yes |  |  | Symantec System Center agent (SSC-AGENT) |
| 2989 | Yes | Yes |  |  | Zarkov Intelligent Agent Communication |
| 3000 | Unofficial |  |  |  | Ruby on Rails development default |
| 3000 | Unofficial |  |  |  | Bun |
| 3000 | Unofficial |  |  |  | Meteor development default |
| 3000 | Unofficial | Unofficial |  |  | Resilio Sync, spun from BitTorrent Sync. |
| 3000 | Unofficial |  |  |  | Create React App, script to create single-page React applications |
| 3000 | Unofficial |  |  |  | Gogs and Gitea (self-hosted Git service) |
| 3000 | Unofficial |  |  |  | Grafana |
| 3001 | Yes |  |  |  | Honeywell Prowatch |
| 3004 | Unofficial |  |  |  | iSync |
| 3010 | Yes | Yes |  |  | KWS Connector |
| 3020 | Yes | Yes |  |  | Common Internet File System (CIFS). See also port 445 for Server Message Block (SMB), a dialect of CIFS. |
| 3050 | Yes | Yes |  |  | gds-db (Interbase/Firebird databases) |
| 3052 | Yes | Yes |  |  | APC PowerChute Network |
| 3074 | Yes | Yes |  |  | Xbox LIVE and Games for Windows – Live |
| 3101 | Unofficial |  |  |  | BlackBerry Enterprise Server communication protocol |
| 3128 | Unofficial |  |  |  | Squid caching web proxy |
| 3225 | Yes | Yes |  |  | Fibre Channel over IP (FCIP) |
| 3233 | Yes | Yes |  |  | WhiskerControl research control protocol |
| 3260 | Yes | Yes |  |  | iSCSI |
| 3268 | Yes | Yes |  |  | msft-gc, Microsoft Global Catalog (LDAP service which contains data from Active Directory forests) |
| 3269 | Yes | Yes |  |  | msft-gc-ssl, Microsoft Global Catalog over SSL (similar to port 3268, LDAP over SSL) |
| 3283 | Yes | Yes |  |  | Net Assistant, a predecessor to Apple Remote Desktop |
| 3283 | Unofficial | Unofficial |  |  | Apple Remote Desktop 2.0 or later |
| 3290 |  | Unofficial |  |  | Virtual Air Traffic Simulation (VATSIM) network voice communication |
| 3305 | Yes | Yes |  |  | Odette File Transfer Protocol (OFTP) |
| 3306 | Yes | Assigned |  |  | MySQL database system |
| 3323 | Unofficial | Unofficial |  |  | DECE GEODI Server |
| 3332 |  | Unofficial |  |  | Thundercloud DataPath Overlay Control |
| 3333 | Unofficial |  |  |  | Eggdrop, an IRC bot default port |
| 3333 | Unofficial |  |  |  | Network Caller ID server |
| 3333 | Unofficial |  |  |  | CruiseControl.rb |
| 3333 | Unofficial |  |  |  | OpenOCD (gdbserver) |
| 3344 | Unofficial | Unofficial |  |  | Repetier-Server |
| 3351 | Unofficial | Unofficial |  |  | Pervasive PSQL |
| 3386 | Yes | Yes |  |  | GTP' 3GPP GSM/UMTS CDR logging protocol |
| 3389 | Yes | Yes |  |  | Microsoft Terminal Server (RDP) officially registered as Windows Based Terminal (WBT) |
| 3396 | Yes | Yes |  |  | Novell NDPS Printer Agent |
| 3412 | Yes | Yes |  |  | xmlBlaster |
| 3423 | Yes |  |  |  | Xware xTrm Communication Protocol |
| 3424 | Yes |  |  |  | Xware xTrm Communication Protocol over SSL |
| 3435 | Yes | Yes |  |  | Pacom Security User Port |
| 3455 | Yes | Yes |  |  | Resource Reservation Protocol (RSVP) |
| 3478 | Yes | Yes |  |  | STUN, a protocol for NAT traversal |
| 3478 | Yes | Yes |  |  | TURN, a protocol for NAT traversal (extension to STUN) |
| 3478 | Yes | Yes |  |  | STUN Behavior Discovery. See also port 5349. |
| 3478 |  | Unofficial |  |  | Microsoft Teams |
| 3479-3480 |  | Unofficial |  |  | Microsoft Teams |
| 3479-3480 | Unofficial | Unofficial |  |  | PlayStation Network |
| 3481 |  | Unofficial |  |  | Microsoft Teams |
| 3483 | Yes |  |  |  | Slim Devices discovery protocol |
| 3483 | Yes |  |  |  | Slim Devices SlimProto protocol |
| 3493 | Yes | Yes |  |  | Network UPS Tools (NUT) |
| 3503 | Yes | Yes |  |  | MPLS LSP-echo Port |
| 3516 | Yes | Yes |  |  | Smartcard Port |
| 3527 |  | Yes |  |  | Microsoft Message Queuing |
| 3535 | Unofficial |  |  |  | SMTP alternate |
| 3544 |  | Yes |  |  | Teredo tunneling |
| 3551 | Yes | Yes |  |  | Apcupsd Information Port |
| 3601 | Yes |  |  |  | SAP Message Server Port |
| 3632 | Yes | Assigned |  |  | Distcc, distributed compiler |
| 3645 | Yes | Yes |  |  | Cyc |
| 3655 | Yes | Yes |  |  | Advanced Systems Concepts, Inc. ActiveBatch Exec Agent |
| 3659 | Yes | Yes |  |  | Apple SASL, used by macOS Server Password Server |
| 3659 | Unofficial |  |  |  | Battlefield 4 |
| 3667 | Yes | Yes |  |  | Information Exchange |
| 3671 | Yes | Yes |  |  | KNXnet/IP(EIBnet/IP) |
| 3689 | Yes | Assigned |  |  | Digital Audio Access Protocol (DAAP), used by Apple's iTunes and AirPlay |
| 3690 | Yes | Yes |  |  | Subversion (SVN) version control system |
| 3702 | Yes | Yes |  |  | Web Services Dynamic Discovery (WS-Discovery), used by various components of Windows Vista and later |
| 3721 | Unofficial |  |  |  | ES File Explorer FTP server |
| 3724 | Yes | Yes |  |  | Some Blizzard games |
| 3724 | Unofficial |  |  |  | Club Penguin Disney online game for kids |
| 3725 | Yes | Yes |  |  | Netia NA-ER Port |
| 3749 | Yes | Yes |  |  | CimTrak registered port |
| 3768 | Yes | Yes |  |  | RBLcheckd server daemon |
| 3784 |  | Yes |  |  | Bidirectional Forwarding Detection (BFD)for IPv4 and IPv6 (Single Hop) (RFC 5881) |
| 3785 |  | Unofficial |  |  | VoIP program used by Ventrilo |
| 3799 |  | Yes |  |  | RADIUS change of authorization |
| 3804 | Yes | Yes |  |  | Harman Professional HiQnet protocol |
| 3825 | Unofficial |  |  |  | RedSeal Networks client/server connection |
| 3826 | Yes | Yes |  |  | WarMUX game server |
| 3826 | Unofficial |  |  |  | RedSeal Networks client/server connection |
| 3830 | Yes | Yes |  |  | System Management Agent, developed and used by Cerner to monitor and manage solutions |
| 3835 | Unofficial |  |  |  | RedSeal Networks client/server connection |
| 3856 | Unofficial | Unofficial |  |  | ERP Server Application used by F10 Software |
| 3868 | Yes |  | Yes |  | Diameter base protocol (RFC 3588) |
| 3872 | Yes |  |  |  | Oracle Enterprise Manager Remote Agent |
| 3880 | Yes | Yes |  |  | IGRS |
| 3900 | Yes |  |  |  | udt_os, IBM UniData UDT OS |
| 3911 | Yes | Yes |  |  | prnstatus, Printer Status Port |
| 3960 |  | Unofficial |  |  | Warframe online interaction |
| 3962 |  | Unofficial |  |  | Warframe online interaction |
| 3978 | Unofficial | Unofficial |  |  | OpenTTD game (masterserver and content service) |
| 3978 | Unofficial |  |  |  | Palo Alto Networks' Panorama management of firewalls and log collectors & pre-PAN-OS 8.0 Panorama-to-managed devices software updates. |
| 3979 | Unofficial | Unofficial |  |  | OpenTTD game |
| 3999 | Yes | Yes |  |  | Norman distributed scanning service |
| 4000 | Unofficial | Unofficial |  |  | Diablo II game |
| 4001 | Unofficial |  |  |  | Microsoft Ants game |
| 4001 | Unofficial |  |  |  | CoreOS etcd client communication |
| 4001 | Unofficial | Unofficial |  |  | InterPlanetary File System swarm node |
| 4018 | Yes | Yes |  |  | Protocol information and warnings |
| 4035 | Unofficial |  |  |  | IBM Rational Developer for System z Remote System Explorer Daemon |
| 4045 | Unofficial | Unofficial |  |  | Solaris lockd NFS lock daemon/manager |
| 4050 | Unofficial |  |  |  | Mud Master Chat protocol (MMCP) – Peer-to-peer communications between MUD clients. |
| 4061 | Yes | Yes |  |  | [https://doc.zeroc.com/ice/3.7/client-server-features/locators Ice Location Service] |
| 4069 |  | Yes |  |  | Minger Email Address Verification Protocol |
| 4070 | Unofficial | Unofficial |  |  | Amazon Echo Dot (Amazon Alexa) streaming connection with Spotify |
| 4089 | Yes | Yes |  |  | OpenCORE Remote Control Service |
| 4090 | Yes | Yes |  |  | Kerio |
| 4093 | Yes | Yes |  |  | PxPlus Client server interface ProvideX |
| 4096 | Yes | Yes |  |  | Ascom Timeplex Bridge Relay Element (BRE) |
| 4105 | Yes | Yes |  |  | Shofar (ShofarNexus) |
| 4111 | Yes | Assigned |  |  | Xgrid |
| 4116 | Yes | Yes |  |  | Smartcard-TLS |
| 4123 | Assigned | Yes |  |  | Z-Wave Protocol |
| 4125 | Unofficial |  |  |  | Microsoft Remote Web Workplace administration |
| 4172 | Yes | Yes |  |  | Teradici PCoIP |
| 4190 | Yes |  |  |  | ManageSieve |
| 4195 | Yes | Yes | Yes | Yes | AWS protocol for cloud remoting solution |
| 4197 | Yes | Yes |  |  | Harman International's HControl protocol for control and monitoring of Audio, Video, Lighting and Control equipment |
| 4198 | Unofficial | Unofficial |  |  | Couch Potato Android app |
| 4200 | Unofficial |  |  |  | Angular app |
| 4201 | Unofficial |  |  |  | TinyMUD and various derivatives |
| 4213 | Unofficial |  |  |  | DuckDB UI default port |
| 4222 | Unofficial |  |  |  | NATS server default port |
| 4226 | Unofficial | Unofficial |  |  | Aleph One, a computer game |
| 4242 | Unofficial |  |  |  | Orthanc – DICOM server |
| 4242 | Unofficial |  |  |  | Quassel distributed IRC client |
| 4243 | Unofficial |  |  |  | Docker implementations, redistributions, and setups default |
| 4243 | Unofficial |  |  |  | CrashPlan |
| 4244 | Unofficial | Unofficial |  |  | Viber |
| 4303 | Yes | Yes |  |  | Simple Railroad Command Protocol (SRCP) |
| 4307 | Yes |  |  |  | TrueConf Client – TrueConf Server media data exchange |
| 4321 | Yes |  |  |  | Referral Whois (RWhois) Protocol |
| 4420 | Yes | Yes |  |  | NVM Express over Fabrics storage access |
| 4433 |  | Unofficial |  |  | SaltoSystems - DTLS Based Communication for NCoder |
| 4444 | Unofficial | Unofficial |  |  | Oracle WebCenter Content: Content Server—Intradoc Socket port. (formerly known as Oracle Universal Content Management). |
| 4444 | Unofficial | Unofficial |  |  | Metasploit's default listener port |
| 4444 | Unofficial | Unofficial |  |  | Xvfb X server virtual frame buffer service |
| 4444 | Unofficial |  |  |  | OpenOCD (Telnet) |
| 4444 | Unofficial |  |  |  | I2P HTTP/S proxy |
| 4445 | Unofficial |  |  |  | I2P HTTP/S proxy |
| 4455 | Unofficial |  |  |  | OBS Studio built-in WebSocket plugin default port |
| 4460 | Yes | Assigned |  |  | Network Time Security Key Establishment (NTS) |
| 4486 | Yes | Yes |  |  | Integrated Client Message Service (ICMS) |
| 4488 | Yes | Assigned |  |  | Apple Wide Area Connectivity Service, used by Back to My Mac |
| 4500 | Assigned | Yes |  |  | IPSec NAT Traversal (RFC 3947, RFC 4306) |
| 4502-4504 | Yes |  |  |  | Microsoft Silverlight connectable ports under non-elevated trust |
| 4505-4506 | Yes |  |  |  | Microsoft Silverlight connectable ports under non-elevated trust |
| 4505-4506 | Unofficial |  |  |  | Salt master |
| 4507-4533 | Yes |  |  |  | Microsoft Silverlight connectable ports under non-elevated trust |
| 4534 | Yes |  |  |  | Microsoft Silverlight connectable ports under non-elevated trust |
| 4534 |  | Unofficial |  |  | Armagetron Advanced server default |
| 4560 | Unofficial |  |  |  | default Log4j socketappender port |
| 4567 | Unofficial |  |  |  | Sinatra default server port in development mode (HTTP) |
| 4569 |  | Yes |  |  | Inter-Asterisk eXchange (IAX2) |
| 4604 | Yes |  |  |  | Identity Registration Protocol |
| 4605 | Yes |  |  |  | Direct End to End Secure Chat Protocol |
| 4610-4640 | Unofficial |  |  |  | QualiSystems TestShell Suite Services |
| 4662 | Yes | Yes |  |  | OrbitNet Message Service |
| 4662 | Unofficial |  |  |  | Default for older versions of eMule |
| 4664 | Unofficial |  |  |  | Google Desktop Search |
| 4672 |  | Unofficial |  |  | Default for older versions of eMule |
| 4711 | Unofficial |  |  |  | eMule optional web interface |
| 4713 | Unofficial |  |  |  | PulseAudio sound server |
| 4723 | Unofficial |  |  |  | Appium open source automation tool |
| 4724 | Unofficial |  |  |  | Default bootstrap port to use on device to talk to Appium |
| 4728 | Yes |  |  |  | Computer Associates Desktop and Server Management (DMP)/Port Multiplexer |
| 4730 | Yes | Yes |  |  | Gearman's job server |
| 4739 | Yes | Yes |  |  | IP Flow Information Export |
| 4747 | Unofficial |  |  |  | Apprentice |
| 4753 | Yes | Yes |  |  | SIMON (service and discovery) |
| 4789 |  | Yes |  |  | Virtual eXtensible Local Area Network (VXLAN) |
| 4791 |  | Yes |  |  | IP Routable RocE (RoCEv2) |
| 4840 | Yes | Yes |  |  | OPC UA Connection Protocol (TCP) and OPC UA Multicast Datagram Protocol (UDP) for OPC Unified Architecture from OPC Foundation |
| 4843 | Yes | Yes |  |  | OPC UA TCP Protocol over TLS/SSL for OPC Unified Architecture from OPC Foundation |
| 4847 | Yes | Yes |  |  | Web Fresh Communication, Quadrion Software & Odorless Entertainment |
| 4848 | Unofficial |  |  |  | Java GlassFish Application Server administration default |
| 4894 | Yes | Yes |  |  | LysKOM Protocol A |
| 4900 | Unofficial | Unofficial |  |  | HFSQL (Hyperfile SQL) Mantra Server from PC SOFT |
| 4944 |  | Unofficial |  |  | DrayTek DSL Status Monitoring |
| 4949 | Yes |  |  |  | Munin Resource Monitoring Tool |
| 4950 | Yes | Yes |  |  | Cylon Controls UC32 Communications Port |
| 5000 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5001 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5001 | Unofficial |  |  |  | Slingbox and Slingplayer |
| 5001 | Unofficial | Unofficial |  |  | Iperf (Tool for measuring TCP and UDP bandwidth performance) |
| 5001 | Unofficial |  |  |  | Synology Inc. Secured Management Console, File Station, Audio Station |
| 5001 | Unofficial |  |  |  | 3CX Phone System Management Console/Web Client (HTTPS) |
| 5001 | Unofficial |  |  |  | InterPlanetary File System RPC API |
| 5002 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5002 | Unofficial |  |  |  | ASSA ARX access control system |
| 5003 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5003 | Yes | Assigned |  |  | FileMaker – name binding and transport |
| 5004 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5004 | Yes | Yes |  | Yes | Real-time Transport Protocol media data (RTP) (RFC 3551, RFC 4571) |
| 5005 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5005 | Yes | Yes |  | Yes | Real-time Transport Protocol control protocol (RTCP) (RFC 3551, RFC 4571) |
| 5006 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5007 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5007 | Unofficial |  |  |  | Palo Alto Networks – User-ID agent |
| 5008-5009 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5010 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5010 | Yes | Yes |  |  | Registered to: TelePath (the IBM FlowMark workflow-management system messaging platform)<br />The TCP port is now used for: IBM WebSphere MQ Workflow |
| 5011 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5011 | Yes | Yes |  |  | TelePath (the IBM FlowMark workflow-management system messaging platform) |
| 5012-5021 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5022 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5022 | Unofficial |  |  |  | MSSQL Server Replication and Database mirroring endpoints |
| 5023-5024 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5025 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5025 | Yes | Yes |  |  | scpi-raw Standard Commands for Programmable Instruments |
| 5026-5028 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5029 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5029 |  | Unofficial |  |  | Sonic Robo Blast 2 and Sonic Robo Blast 2 Kart servers |
| 5030 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5031 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5031 | Unofficial | Unofficial |  |  | AVM CAPI-over-TCP (ISDN over Ethernet tunneling) |
| 5032-5036 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5037 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5037 | Unofficial |  |  |  | Android ADB server |
| 5038-5043 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5044 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5044 | Yes |  |  |  | Standard port in Filebeats/Logstash implementation of Lumberjack protocol. |
| 5045-5047 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5048 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5048 | Yes |  |  |  | Texai Message Service |
| 5049 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5050 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5050 | Unofficial |  |  |  | Yahoo! Messenger |
| 5051 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5051 | Yes |  |  |  | ita-agent Symantec Intruder Alert |
| 5052-5059 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5060 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5060 | Yes | Yes |  |  | Session Initiation Protocol (SIP) |
| 5061 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5061 | Yes |  |  |  | Session Initiation Protocol (SIP) over TLS |
| 5062 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5062 | Yes | Yes |  |  | Localisation access |
| 5063 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5064 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5064 | Yes | Yes |  |  | EPICS Channel Access server |
| 5065 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5065 | Assigned | Yes |  |  | EPICS Channel Access repeater beacon |
| 5066-5069 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5070 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5070 | Unofficial |  |  |  | Binary Floor Control Protocol (BFCP) |
| 5071-5074 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5075 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5075 | Yes |  |  |  | EPICS PV Access Data |
| 5076 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5076 |  | Yes |  |  | EPICS PV Access Searches |
| 5077-5079 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5080 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5080 | Unofficial | Unofficial |  |  | NEC Phone System SV8100 and SV9100 MLC phones: default iSIP port |
| 5081-5083 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5084 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5084 | Yes | Yes |  |  | EPCglobal Low Level Reader Protocol (LLRP) |
| 5085 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5085 | Yes | Yes |  |  | EPCglobal Low Level Reader Protocol (LLRP) over TLS |
| 5086-5089 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5090 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5090 | Unofficial | Unofficial |  |  | 3CX Phone System 3CX Tunnel Protocol, 3CX App API, 3CX Session Border Controller |
| 5091-5092 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5093 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5093 |  | Yes |  |  | Thales Sentinel (was SafeNet, Gemalto), Sentinel LM / Sentinel RMS, client-to-server |
| 5094-5098 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5099 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5099 | Yes | Yes |  |  | Thales Sentinel (was SafeNet, Gemalto), Sentinel LM / Sentinel RMS, server-to-server |
| 5100-5103 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5104 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5104 | Unofficial |  |  |  | IBM Tivoli Framework NetCOOL/Impact HTTP Service |
| 5105-5120 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5121 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5121 | Unofficial |  |  |  | Neverwinter Nights |
| 5122-5149 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5150 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5150 | Yes | Yes |  |  | ATMP Ascend Tunnel Management Protocol |
| 5151 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5151 | Yes |  |  |  | ESRI SDE Instance |
| 5151 | Yes |  |  |  | ESRI SDE Remote Start |
| 5152-5153 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5154 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5154 | Yes | Yes |  |  | BZFlag |
| 5155-5171 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5172 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5172 | Yes |  |  |  | PC over IP Endpoint Management |
| 5173 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5173 | Unofficial |  |  |  | Vite |
| 5174-5189 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5190 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5190 | Yes | Yes |  |  | AOL Instant Messenger protocol. |
| 5191-5197 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5198-5199 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5198-5199 |  | Unofficial |  |  | EchoLink VoIP Amateur Radio Software (Voice) |
| 5200 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5200 | Unofficial |  |  |  | EchoLink VoIP Amateur Radio Software (Information) |
| 5201 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5201 | Unofficial | Unofficial |  |  | Iperf3 (Tool for measuring TCP and UDP bandwidth performance) |
| 5202-5221 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5222 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5222 | Yes | Reserved |  |  | Extensible Messaging and Presence Protocol (XMPP) client connection |
| 5223 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5223 | Unofficial |  |  |  | Apple Push Notification Service |
| 5223 | Unofficial |  |  |  | Extensible Messaging and Presence Protocol (XMPP) client connection over SSL |
| 5224-5227 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5228 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5228 | Yes |  |  |  | HP Virtual Room Service |
| 5228 | Unofficial |  |  |  | Google Play, Android Cloud to Device Messaging Service, Google Cloud Messaging |
| 5229-5230 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5231 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5231 | Yes |  |  |  | Remote Control of Scan Software for Cruse Scanners |
| 5232 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5232 | Yes |  |  |  | Cruse Scanning System Service |
| 5232 | Unofficial |  |  |  | Silicon Graphics Distributed Graphics Library daemon (dgld) |
| 5233-5234 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5235-5236 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5235-5236 | Unofficial |  |  |  | Firebase Cloud Messaging |
| 5237-5241 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5242-5243 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5242-5243 | Unofficial | Unofficial |  |  | Viber |
| 5244-5245 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5246 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5246 |  | Yes |  |  | Control And Provisioning of Wireless Access Points (CAPWAP) CAPWAP control |
| 5247 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5247 |  | Yes |  |  | Control And Provisioning of Wireless Access Points (CAPWAP) CAPWAP data |
| 5248-5268 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5269 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5269 | Yes |  |  |  | Extensible Messaging and Presence Protocol (XMPP) server-to-server connection |
| 5270-5279 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5280 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5280 | Yes |  |  |  | Extensible Messaging and Presence Protocol (XMPP) |
| 5281 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5281 | Unofficial |  |  |  | Extensible Messaging and Presence Protocol (XMPP) |
| 5282-5297 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5298 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5298 | Yes | Yes |  |  | Extensible Messaging and Presence Protocol (XMPP) |
| 5299-5309 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5310 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5310 | Assigned | Yes |  |  | Outlaws, a 1997 first-person shooter video game |
| 5311-5317 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5318 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5318 | Yes | Reserved |  |  | Certificate Management over CMS |
| 5319-5348 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5349 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5349 | Yes | Yes |  |  | STUN over TLS/DTLS, a protocol for NAT traversal |
| 5349 | Yes | Yes |  |  | TURN over TLS/DTLS, a protocol for NAT traversal |
| 5349 | Yes | Reserved |  |  | STUN Behavior Discovery over TLS. See also port 3478. |
| 5350 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5351 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5351 | Reserved | Yes |  |  | NAT Port Mapping Protocol and Port Control Protocol—client-requested configuration for connections through network address translators and firewalls |
| 5352 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5353 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5353 | Assigned | Yes |  |  | Multicast DNS (mDNS) |
| 5354 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5355 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5355 | Yes | Yes |  |  | Link-Local Multicast Name Resolution (LLMNR), allows hosts to perform name resolution for hosts on the same local link (only provided by Windows Vista and Server 2008) |
| 5356 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5357 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5357 | Unofficial | Unofficial |  |  | Web Services for Devices (WSDAPI) (starting from Windows Vista, Windows 7 and Server 2008) |
| 5358 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5358 | Unofficial | Unofficial |  |  | WSDAPI Applications to Use a Secure Channel (only provided by Windows Vista, Windows 7 and Server 2008) |
| 5359-5393 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5394 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5394 |  | Unofficial |  |  | Kega Fusion, a Sega multi-console emulator |
| 5395-5401 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5402 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5402 | Yes | Yes |  |  | Multicast File Transfer Protocol (MFTP) |
| 5403-5404 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5405 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5405 | Yes | Yes |  |  | NetSupport Manager |
| 5406-5411 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5412 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5412 | Yes | Yes |  |  | IBM Rational Synergy (Telelogic Synergy) (Continuus CM) Message Router |
| 5413 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5413 | Yes | Yes |  |  | Wonderware SuiteLink service |
| 5414-5416 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5417 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5417 | Yes | Yes |  |  | SNS Agent |
| 5418-5420 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5421 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5421 | Yes | Yes |  |  | NetSupport Manager |
| 5422-5431 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5432 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5432 | Yes | Assigned |  |  | PostgreSQL database system |
| 5433 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5433 | Unofficial |  |  |  | Bouwsoft file/webserver |
| 5434-5444 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5445 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5445 |  | Unofficial |  |  | Cisco Unified Video Advantage |
| 5446-5449 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5450 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5450 | Unofficial | Unofficial |  |  | OSIsoft PI Server Client Access |
| 5451-5456 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5457 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5457 | Unofficial |  |  |  | OSIsoft PI Asset Framework Client Access |
| 5458 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5458 | Unofficial |  |  |  | OSIsoft PI Notifications Client Access |
| 5459-5479 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5480 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5480 | Unofficial |  |  |  | VMware VAMI (Virtual Appliance Management Infrastructure)—used for initial setup of various administration settings on Virtual Appliances designed using the VAMI architecture. |
| 5481 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5481 | Unofficial |  |  |  | Schneider Electric's ClearSCADA (SCADA implementation for Windows) — used for client-to-server communication. |
| 5482-5494 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5495 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5495 | Unofficial |  |  |  | IBM Cognos TM1 Admin server |
| 5496-5497 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5498 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5498 | Unofficial |  |  |  | Hotline tracker server connection |
| 5499 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5499 |  | Unofficial |  |  | Hotline tracker server discovery |
| 5500 |  | Unofficial |  |  | League of Legends, a multiplayer online battle arena video game |
| 5500 | Unofficial |  |  |  | Hotline control connection |
| 5500 | Unofficial |  |  |  | VNC Remote Frame Buffer RFB protocol—for incoming listening viewer |
| 5501 | Unofficial |  |  |  | Hotline file transfer connection |
| 5517 | Unofficial |  |  |  | Setiqueue Proxy server client for SETI@Home project |
| 5520 |  | Unofficial |  |  | Hytale multiplayer server |
| 5550 | Unofficial |  |  |  | Hewlett-Packard Data Protector |
| 5554 | Unofficial | Unofficial |  |  | Fastboot default wireless port |
| 5555 | Unofficial | Unofficial |  |  | Oracle WebCenter Content: Inbound Refinery—Intradoc Socket port. (formerly known as Oracle Universal Content Management). Port though often changed during installation |
| 5555 | Unofficial |  |  |  | Freeciv versions up to 2.0, Hewlett-Packard Data Protector, McAfee EndPoint Encryption Database Server, SAP, Default for Microsoft Dynamics CRM 4.0, Softether VPN default port |
| 5555 | Unofficial |  |  |  | Wireless adb (Android Debug Bridge) control of an Android device over the network. |
| 5556 | Yes | Yes |  |  | Freeciv, Oracle WebLogic Server Node Manager |
| 5568 | Yes | Yes |  |  | Session Data Transport (SDT), a part of Architecture for Control Networks (ACN) |
| 5601 | Unofficial |  |  |  | Kibana |
| 5631 | Yes |  |  |  | pcANYWHEREdata, Symantec pcAnywhere (version 7.52 and later) data |
| 5632 |  | Yes |  |  | pcANYWHEREstat, Symantec pcAnywhere (version 7.52 and later) status |
| 5656 | Unofficial |  |  |  | IBM Lotus Sametime p2p file transfer |
| 5666 | Unofficial |  |  |  | NRPE (Nagios) |
| 5667 | Unofficial |  |  |  | NSCA (Nagios) |
| 5670 | Yes |  |  |  | FILEMQ ZeroMQ File Message Queuing Protocol |
| 5670 | Yes |  |  |  | ZRE-DISC ZeroMQ Realtime Exchange Protocol (Discovery) |
| 5671 | Yes | Assigned |  |  | Advanced Message Queuing Protocol (AMQP) over TLS |
| 5672 | Yes | Assigned | Yes |  | Advanced Message Queuing Protocol (AMQP) |
| 5683 | Yes | Yes |  |  | Constrained Application Protocol (CoAP) |
| 5684 | Yes | Yes |  |  | Constrained Application Protocol Secure (CoAPs) |
| 5693 | Unofficial |  |  |  | Nagios Cross Platform Agent (NCPA) |
| 5701 | Unofficial |  |  |  | Hazelcast default communication port |
| 5718 | Unofficial |  |  |  | Microsoft DPM Data Channel (with the agent coordinator) |
| 5719 | Unofficial |  |  |  | Microsoft DPM Data Channel (with the protection agent) |
| 5722 | Yes | Yes |  |  | Microsoft RPC, DFSR (SYSVOL) Replication Service |
| 5723 | Unofficial |  |  |  | System Center Operations Manager |
| 5724 | Unofficial |  |  |  | Operations Manager Console |
| 5741 | Yes | Yes |  |  | IDA Discover Port 1 |
| 5742 | Yes | Yes |  |  | IDA Discover Port 2 |
| 5800 | Unofficial |  |  |  | VNC Remote Frame Buffer RFB protocol over HTTP |
| 5800 | Unofficial |  |  |  | ProjectWise Server |
| 5900 | Yes | Yes |  |  | Remote Frame Buffer protocol (RFB) |
| 5900 | Unofficial |  |  |  | Virtual Network Computing (VNC) Remote Frame Buffer RFB protocol |
| 5905 | Unofficial |  |  |  | Windows service "C:\Program Files\Intel\Intel(R) Online Connect Access\IntelTechnologyAccessService.exe" that listens on 127.0.0.1 |
| 5931 | Yes | Yes |  |  | AMMYY admin Remote Control |
| 5938 | Unofficial | Unofficial |  |  | TeamViewer remote desktop protocol |
| 5984 | Yes | Yes |  |  | CouchDB database server |
| 5985 | Yes |  |  |  | Windows PowerShell Default psSession Port Windows Remote Management Service (WinRM-HTTP) |
| 5986 | Yes |  |  |  | Windows PowerShell Default psSession Port Windows Remote Management Service (WinRM-HTTPS) |
| 5988-5989 | Yes |  |  |  | CIM-XML (DMTF Protocol) |
| 6000-6004 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6005 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6005 | Unofficial |  |  |  | Default for BMC Software Control-M/Server—Socket used for communication between Control-M processes—though often changed during installation |
| 6005 | Unofficial |  |  |  | Default for Camfrog chat & cam client |
| 6006-6008 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6009 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6009 | Unofficial |  |  |  | JD Edwards EnterpriseOne ERP system JDENet messaging client listener |
| 6010-6023 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6024-6025 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6024-6025 |  | Unofficial |  |  | Tigermeeting Android client discovery |
| 6026 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6026 | Unofficial |  |  |  | Tigermeeting client/server communication |
| 6027-6029 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6030-6031 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6030-6031 |  | Unofficial |  |  | Tigermeeting Admin user discovery |
| 6032 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6032 | Unofficial |  |  |  | Tigermeeting API for cloud management - TigerDriver |
| 6033-6049 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6050-6051 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6050-6051 | Unofficial |  |  |  | Arcserve backup |
| 6052-6063 | Yes | Yes |  |  | X11—used between an X client and server over the network |
| 6081 |  | Yes |  |  | Generic Network Virtualization Encapsulation (Geneve) |
| 6086 | Yes |  |  |  | Peer Distributed Transfer Protocol (PDTP), FTP like file server in a P2P network |
| 6100 | Unofficial |  |  |  | Vizrt System |
| 6100 | Unofficial |  |  |  | Ventrilo authentication for version 3 |
| 6101 | Unofficial |  |  |  | Backup Exec Agent Browser |
| 6110 | Yes | Yes |  |  | softcm, HP Softbench CM |
| 6111 | Yes | Yes |  |  | spc, HP Softbench Sub-Process Control |
| 6112 | Yes | Yes |  |  | dtspcd, execute commands and launch applications remotely |
| 6112 | Unofficial | Unofficial |  |  | Blizzard's Battle.net gaming service and some games, ArenaNet gaming service, Relic gaming service |
| 6112 | Unofficial |  |  |  | Club Penguin Disney online game for kids |
| 6113 | Unofficial |  |  |  | Club Penguin Disney online game for kids, Used by some Blizzard games |
| 6121-6122 | Unofficial | Unofficial |  |  | Lacewing networking extensions used in Clickteam Fusion. |
| 6136 | Unofficial |  |  |  | ObjectDB database server |
| 6159 | Yes |  |  |  | ARINC 840 EFB Application Control Interface |
| 6160 | Unofficial |  |  |  | Veeam Installer Service |
| 6161 | Unofficial |  |  |  | Veeam vPower NFS Service |
| 6162 | Unofficial |  |  |  | Veeam Data Mover |
| 6163 | Unofficial |  |  |  | Veeam Hyper-V Integration Service |
| 6164 | Unofficial |  |  |  | Veeam WAN Accelerator |
| 6165 | Unofficial |  |  |  | Veeam WAN Accelerator Data Transfer |
| 6167 | Unofficial |  |  |  | Veeam Log Shipping Service |
| 6170 | Unofficial |  |  |  | Veeam Mount Server |
| 6200 | Unofficial |  |  |  | Oracle WebCenter Content Portable: Content Server (With Native UI) and Inbound Refinery |
| 6201 | Assigned | Assigned |  |  | Thermo-Calc Software AB: Management of service nodes in a processing grid for thermodynamic calculations |
| 6201 | Unofficial |  |  |  | Oracle WebCenter Content Portable: Admin |
| 6225 | Unofficial |  |  |  | Oracle WebCenter Content Portable: Content Server Web UI |
| 6227 | Unofficial |  |  |  | Oracle WebCenter Content Portable: JavaDB |
| 6240 | Unofficial |  |  |  | Oracle WebCenter Content Portable: Capture |
| 6244 | Unofficial | Unofficial |  |  | Oracle WebCenter Content Portable: Content Server—Intradoc Socket port |
| 6255 | Unofficial | Unofficial |  |  | Oracle WebCenter Content Portable: Inbound Refinery—Intradoc Socket port |
| 6257 |  | Unofficial |  |  | WinMX (see also 6699) |
| 6260 | Unofficial | Unofficial |  |  | planet M.U.L.E. |
| 6262 | Unofficial |  |  |  | Sybase Advantage Database Server |
| 6343 |  | Yes |  |  | SFlow, sFlow traffic monitoring |
| 6346 | Yes | Yes |  |  | gnutella-svc, gnutella (FrostWire, Limewire, Shareaza, etc.) |
| 6347 | Yes | Yes |  |  | gnutella-rtr, Gnutella alternate |
| 6350 | Yes | Yes |  |  | App Discovery and Access Protocol |
| 6379 | Yes |  |  |  | Redis key-value data store |
| 6389 | Unofficial |  |  |  | EMC CLARiiON |
| 6432 | Yes |  |  |  | PgBouncer—A connection pooler for PostgreSQL |
| 6436 | Unofficial |  |  |  | Leap Motion Websocket Server TLS |
| 6437 | Unofficial |  |  |  | Leap Motion Websocket Server |
| 6443 | Unofficial |  |  |  | Kubernetes API server |
| 6444 | Yes | Yes |  |  | Sun Grid Engine Qmaster Service |
| 6445 | Yes | Yes |  |  | Sun Grid Engine Execution Service |
| 6454 |  | Unofficial |  |  | Art-Net protocol |
| 6463 | Unofficial |  |  |  | Discord RPC |
| 6464 | Unofficial |  |  |  | Discord RPC |
| 6464 | Yes | Yes |  |  | Port assignment for medical device communication in accordance to IEEE 11073-20701 |
| 6465-6472 | Unofficial |  |  |  | Discord RPC |
| 6513 | Yes |  |  |  | NETCONF over TLS |
| 6514 | Yes |  |  |  | Syslog over TLS |
| 6515 | Yes | Yes |  |  | Elipse RPC Protocol (REC) |
| 6516 | Unofficial | Unofficial |  |  | Windows Admin Center |
| 6543 | Unofficial |  |  |  | Pylons project#Pyramid Default Pylons Pyramid web service port |
| 6556 | Unofficial |  |  |  | Check MK Agent |
| 6560-6561 | Unofficial |  |  |  | Speech-Dispatcher daemon |
| 6566 | Yes |  |  |  | SANE (Scanner Access Now Easy)—SANE network scanner daemon |
| 6567 | Unofficial |  |  |  | Mindustry multiplayer server |
| 6571 | Unofficial | Unofficial |  |  | Windows Live FolderShare client |
| 6600 | Yes |  |  |  | Microsoft Hyper-V Live |
| 6600 | Unofficial |  |  |  | Music Player Daemon (MPD) |
| 6601 | Yes |  |  |  | Microsoft Forefront Threat Management Gateway |
| 6602 | Yes |  |  |  | Microsoft Windows WSS Communication |
| 6619 | Yes | Yes |  |  | odette-ftps, Odette File Transfer Protocol (OFTP) over TLS/SSL |
| 6622 | Yes | Yes |  |  | Multicast FTP |
| 6626 | Yes | Yes |  |  | Semaphore Messenger |
| 6653 | Yes | Assigned |  |  | OpenFlow |
| 6660-6664 | Unofficial |  |  |  | Internet Relay Chat (IRC) |
| 6665-6669 | Yes |  |  |  | Internet Relay Chat (IRC) |
| 6679 | Yes | Yes |  |  | Osorno Automation Protocol (OSAUT) |
| 6679 | Unofficial |  |  |  | Internet Relay Chat (IRC) SSL (Secure Internet Relay Chat)—often used |
| 6690 | Unofficial |  |  |  | Synology Cloud station |
| 6697 | Yes |  |  |  | IRC SSL (Secure Internet Relay Chat)—often used |
| 6699 | Unofficial |  |  |  | WinMX (see also 6257) |
| 6715 | Unofficial |  |  |  | AberMUD and derivatives default port |
| 6771 |  | Unofficial |  |  | BitTorrent Local Peer Discovery |
| 6783-6785 | Unofficial |  |  |  | Splashtop Remote server broadcast |
| 6789 | Unofficial |  |  |  | Ubiquiti UniFi Network server mobile speed test |
| 6801 | Yes | Yes |  |  | ACNET Control System Protocol |
| 6881-6887 | Unofficial | Unofficial |  |  | BitTorrent beginning of range of ports used most often |
| 6888 | Yes | Yes |  |  | MUSE |
| 6888 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6889-6890 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6891-6900 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6891-6900 | Unofficial | Unofficial |  |  | Windows Live Messenger (File transfer) |
| 6901 | Unofficial | Unofficial |  |  | Windows Live Messenger (Voice) |
| 6901 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6902-6923 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6924 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6924 | Yes | Yes |  |  | split-ping, ping with RX/TX latency/loss split |
| 6925-6934 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6935 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6935 | Yes | Yes |  |  | EthoScan Service |
| 6936 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6936 | Yes | Yes |  |  | XenSource Management Service |
| 6937-6968 | Unofficial | Unofficial |  |  | BitTorrent continuation of range of ports used most often |
| 6969 | Yes | Yes |  |  | acmsoda |
| 6969 | Unofficial | Unofficial |  |  | BitTorrent tracker |
| 6970-6979 | Unofficial | Unofficial |  |  | BitTorrent end of range of ports used most often |
| 6970-6979 | Unofficial |  |  |  | QuickTime Streaming Server |
| 6980 | Unofficial | Unofficial |  |  | BitTorrent end of range of ports used most often |
| 6980 | Unofficial |  |  |  | QuickTime Streaming Server |
| 6980 |  | Unofficial |  |  | Voicemeeter VBAN network audio protocol |
| 6981-6999 | Unofficial | Unofficial |  |  | BitTorrent end of range of ports used most often |
| 6981-6999 | Unofficial |  |  |  | QuickTime Streaming Server |
| 7001 | Unofficial |  |  |  | Avira Server Management Console |
| 7001 | Unofficial |  |  |  | Default for BEA WebLogic Server's HTTP server, though often changed during installation |
| 7002 | Unofficial |  |  |  | Default for BEA WebLogic Server's HTTPS server, though often changed during installation |
| 7005 | Unofficial |  |  |  | Default for BMC Software Control-M/Server and Control-M/Agent for Agent-to-Server, though often changed during installation |
| 7006 | Unofficial |  |  |  | Default for BMC Software Control-M/Server and Control-M/Agent for Server-to-Agent, though often changed during installation |
| 7022 | Unofficial |  |  |  | MSSQL Server Replication and Database mirroring endpoints |
| 7023 |  | Yes |  |  | T2-NMCS Protocol for SatCom Modems |
| 7025 | Unofficial |  |  |  | Zimbra LMTP [mailbox]—local mail delivery |
| 7047 | Unofficial |  |  |  | Zimbra conversion server |
| 7070 | Unofficial | Unofficial |  |  | Real Time Streaming Protocol (RTSP), used by QuickTime Streaming Server. TCP is used by default, UDP is used as an alternate. |
| 7077 | Yes | Yes |  |  | Development-Network Authentification-Protocol |
| 7133 | Unofficial |  |  |  | Enemy Territory: Quake Wars |
| 7144-7145 | Unofficial |  |  |  | [Peer Cast]|Peercast |
| 7171 | Unofficial |  |  |  | Tibia |
| 7262 | Yes | Yes |  |  | CNAP (Calypso Network Access Protocol) |
| 7272 | Yes | Yes |  |  | WatchMe – WatchMe Monitoring |
| 7306 | Unofficial |  |  |  | Zimbra mysql [mailbox] |
| 7307 | Unofficial |  |  |  | Zimbra mysql [logger] |
| 7312 |  | Unofficial |  |  | Sibelius License Server |
| 7396 | Unofficial |  |  |  | Web control interface for Folding@home v7.3.6 and later |
| 7400 | Yes | Yes |  |  | RTPS (Real Time Publish Subscribe) DDS Discovery |
| 7401 | Yes | Yes |  |  | RTPS (Real Time Publish Subscribe) DDS User-Traffic |
| 7402 | Yes | Yes |  |  | RTPS (Real Time Publish Subscribe) DDS Meta-Traffic |
| 7471 | Unofficial |  |  |  | Stateless Transport Tunneling (STT) |
| 7473 | Yes |  |  |  | Rise: The Vieneo Province |
| 7474 | Yes |  |  |  | Neo4J Server webadmin |
| 7478 | Yes |  |  |  | Default port used by Open iT Server. |
| 7542 | Yes | Yes |  |  | Saratoga file transfer protocol |
| 7547 | Yes | Yes |  |  | CPE WAN Management Protocol (CWMP) Technical Report 069 |
| 7575 |  | Unofficial |  |  | Populous: The Beginning server |
| 7624 | Yes | Yes |  |  | Instrument Neutral Distributed Interface |
| 7631 | Yes |  |  |  | ERLPhase |
| 7634 | Unofficial |  |  |  | hddtemp—Utility to monitor hard drive temperature |
| 7652-7654 | Unofficial |  |  |  | I2P anonymizing overlay network |
| 7655 |  | Unofficial |  |  | I2P SAM Bridge Socket API |
| 7656-7658 | Unofficial |  |  |  | I2P anonymizing overlay network |
| 7659 | Unofficial |  |  |  | I2P anonymizing overlay network |
| 7659 | Unofficial | Unofficial |  |  | Polypheny User Interface (database system) |
| 7660 | Unofficial |  |  |  | I2P anonymizing overlay network |
| 7670 | Unofficial |  |  |  | BrettspielWelt BSW Boardgame Portal |
| 7680 | Unofficial |  |  |  | Delivery Optimization for Windows 10 |
| 7687 | Yes |  |  |  | Bolt database connection |
| 7707-7708 |  | Unofficial |  |  | Killing Floor |
| 7717 |  | Unofficial |  |  | Killing Floor |
| 7745 | Unofficial |  |  |  | HomeBox |
| 7777 | Unofficial |  |  |  | iChat server file transfer proxy |
| 7777 | Unofficial |  |  |  | Oracle Cluster File System 2 |
| 7777 | Unofficial |  |  |  | Windows backdoor program tini.exe default |
| 7777 | Unofficial |  |  |  | Just Cause 2: Multiplayer Mod Server |
| 7777 | Unofficial |  |  |  | Terraria default server |
| 7777 | Unofficial | Unofficial |  |  | Super Foosball multiplayer gameplay port |
| 7777 | Unofficial |  |  |  | San Andreas Multiplayer (SA-MP) default port server |
| 7777 | Unofficial |  |  |  | SCP: Secret Laboratory Multiplayer Server |
| 7777 | Yes |  |  |  | Steam common default game server ports (Ark, L4D2, etc.) |
| 7777 | Unofficial | Unofficial |  |  | Unreal Tournament series default server |
| 7778-7788 | Yes |  |  |  | Steam common default game server ports (Ark, L4D2, etc.) |
| 7778-7788 | Unofficial | Unofficial |  |  | Unreal Tournament series default server |
| 7831 | Unofficial |  |  |  | Default used by Smartlaunch Internet Cafe Administration software |
| 7880 | Yes | Yes |  |  | PowerSchool Gradebook Server |
| 7890 | Unofficial |  |  |  | Default that will be used by the iControl Internet Cafe Suite Administration software |
| 7915 | Unofficial |  |  |  | Default for YSFlight server |
| 7935 | Unofficial |  |  |  | Fixed port used for Adobe Flash Debug Player to communicate with a debugger (Flash IDE, Flex Builder or fdb). |
| 7946 | Unofficial | Unofficial |  |  | Docker Swarm communication among nodes |
| 7979 |  | Unofficial |  |  | Used by SilverBluff Studios for communication between servers and clients. |
| 7990 | Unofficial |  |  |  | Atlassian Bitbucket (default port) |
| 8000 | Unofficial |  |  |  | Deno |
| 8000 | Unofficial |  |  |  | Commonly used for Internet radio streams such as SHOUTcast, Icecast and iTunes Radio |
| 8000 | Unofficial | Unofficial |  |  | DynamoDB Local |
| 8000 | Unofficial | Unofficial |  |  | Django Development Webserver |
| 8000 | Unofficial | Unofficial |  |  | Python 3 http.server |
| 8005 | Unofficial |  |  |  | Tomcat remote shutdown |
| 8005 | Unofficial |  |  |  | PLATO ASCII protocol (RFC 600) |
| 8005 | Unofficial |  |  |  | Windows SCCM HTTP listener service |
| 8006 | Unofficial |  |  |  | Quest AppAssure 5 API |
| 8006 | Unofficial |  |  |  | Proxmox Virtual Environment admin web interface |
| 8007 | Unofficial |  |  |  | Quest AppAssure 5 Engine |
| 8007 | Yes |  |  |  | Proxmox Backup Server admin web interface |
| 8008 | Unofficial | Unofficial |  |  | Alternative port for HTTP. See also ports 80 and 8080. |
| 8008 | Unofficial |  |  |  | IBM HTTP Server administration default |
| 8008 | Unofficial |  |  |  | iCal, a calendar application by Apple |
| 8008 | Unofficial |  |  |  | Matrix homeserver federation over HTTP |
| 8009 | Unofficial |  |  |  | Apache JServ Protocol (<code>ajp13</code>) |
| 8010 | Unofficial |  |  |  | Buildbot web status page |
| 8042 | Unofficial | Unofficial |  |  | Orthanc – REST API over HTTP |
| 8061 | Yes | Reserved |  |  | Nikatron Device Protocol (nikatron-dev) |
| 8069 | Unofficial |  |  |  | OpenERP 5.0 XML-RPC protocol |
| 8070 | Unofficial |  |  |  | OpenERP 5.0 NET-RPC protocol |
| 8074 | Yes | Yes |  |  | Gadu-Gadu |
| 8075 | Unofficial |  |  |  | Killing Floor web administration interface |
| 8080 | Yes | Yes |  |  | Alternative port for HTTP. See also ports 80 and 8008. |
| 8080 | Unofficial |  |  |  | Apache Tomcat |
| 8080 | Unofficial |  |  |  | Atlassian JIRA applications |
| 8081 | Yes | Yes |  |  | Sun Proxy Admin Service |
| 8088 | Unofficial |  |  |  | Asterisk management access via HTTP |
| 8088 | Unofficial |  |  |  | YARN ResourceManager Web UI |
| 8089 | Unofficial |  |  |  | Splunk daemon management |
| 8089 | Unofficial |  |  |  | Fritz!Box automatic TR-069 configuration |
| 8090 | Unofficial | Unofficial |  |  | Atlassian Confluence |
| 8090 | Unofficial |  |  |  | Coral Content Distribution Network (legacy; 80 and 8080 now supported) |
| 8090 | Unofficial | Unofficial |  |  | Matrix identity server |
| 8091 | Unofficial | Unofficial |  |  | CouchBase web administration |
| 8092 | Unofficial | Unofficial |  |  | CouchBase API |
| 8093 | Unofficial |  |  |  | GitLab Runner session server |
| 8096 | Unofficial |  |  |  | Emby and Jellyfin HTTP port |
| 8100 | Unofficial |  |  |  | SaltoSystems - Pro Access Space Service |
| 8100 | Unofficial |  |  |  | BlueMap, a 3D Minecraft web viewer and mapping tool |
| 8102 | Unofficial |  |  |  | SaltoSystems - Used for LocalIO-Bridge for USB-Devices |
| 8111 | Unofficial |  |  |  | JOSM Remote Control |
| 8112 | Unofficial |  |  |  | PAC Pacifica Coin |
| 8116 |  | Unofficial |  |  | Check Point Cluster Control Protocol |
| 8118 | Yes |  |  |  | Privoxy—advertisement-filtering Web proxy |
| 8125 | Unofficial |  |  |  | StatsD server |
| 8139 | Unofficial |  |  |  | Puppet (software) Client agent |
| 8140 | Yes |  |  |  | Puppet (software) Master server |
| 8172 | Unofficial |  |  |  | Microsoft Remote Administration for IIS Manager |
| 8181 | Unofficial |  |  |  | FRITZ!Box services |
| 8182 | Unofficial |  |  |  | FRITZ!Box services |
| 8182 | Unofficial |  |  |  | NexusM Media Server HTTP port |
| 8183 | Unofficial |  |  |  | FRITZ!Box services |
| 8184 | Unofficial |  |  |  | FRITZ!Box services |
| 8184 | Unofficial |  |  |  | NCSA Brown Dog Data Access Proxy |
| 8185-8186 | Unofficial |  |  |  | FRITZ!Box services |
| 8188 | Unofficial |  |  |  | ComfyUI Web Interface |
| 8194-8195 | Yes | Yes |  |  | Bloomberg Terminal |
| 8200 | Unofficial |  |  |  | GoToMyPC |
| 8200 | Unofficial |  |  |  | MiniDLNA media server Web Interface |
| 8200 | Unofficial |  |  |  | Elastic APM Server |
| 8222 | Unofficial | Unofficial |  |  | VMware VI Web Access via HTTP |
| 8236 | Unofficial | Unofficial |  |  | jRCS listener for Rocket Software jBASE Remote Connectivity Server |
| 8243 | Yes | Yes |  |  | HTTPS listener for Apache Synapse |
| 8245 | Unofficial |  |  |  | Dynamic DNS for at least No-IP and DynDNS |
| 8280 | Yes | Yes |  |  | HTTP listener for Apache Synapse |
| 8281 | Unofficial |  |  |  | HTTP Listener for Gatecraft Plugin |
| 8291 | Unofficial |  |  |  | WinBox: Mikrotik RouterOS GUI Configurator |
| 8303 |  | Unofficial |  |  | Teeworlds Server |
| 8322 | Assigned | Assigned |  |  | Garmin Marine |
| 8332 | Unofficial |  |  |  | Bitcoin JSON-RPC server |
| 8333 | Unofficial |  |  |  | Bitcoin |
| 8333 | Unofficial | Unofficial |  |  | VMware VI Web Access via HTTPS |
| 8334 | Unofficial |  |  |  | Filestash server (default) |
| 8335 | Unofficial |  |  |  | DBCalm Open |
| 8337 | Unofficial |  |  |  | VisualSVN Distributed File System Service (VDFS) |
| 8384 | Unofficial |  |  |  | Syncthing web GUI |
| 8388 | Unofficial |  |  |  | Shadowsocks proxy server |
| 8400 | Yes |  |  |  | Commvault Communications Service (GxCVD, found in all client computers) |
| 8401 | Yes |  |  |  | Commvault Server Event Manager (GxEvMgrS, available in CommServe) |
| 8403 | Yes |  |  |  | Commvault Firewall (GxFWD, tunnel port for HTTP/HTTPS) |
| 8443 | Unofficial |  |  |  | SW Soft Plesk Control Panel |
| 8443 | Unofficial |  |  |  | Apache Tomcat SSL |
| 8443 | Unofficial |  |  |  | Promise WebPAM SSL |
| 8443 | Unofficial |  |  |  | iCal over SSL |
| 8443 | Unofficial |  |  |  | MineOs WebUi |
| 8448 | Yes | Yes |  |  | Matrix homeserver federation over HTTPS |
| 8484 | Unofficial |  |  |  | MapleStory Login Server |
| 8500 | Unofficial |  |  |  | Adobe ColdFusion built-in web server |
| 8501 | Unofficial |  |  |  | Streamlit Open-source Python framework for machine learning and data science |
| 8530 | Unofficial | Unofficial |  |  | Windows Server Update Services over HTTP, when using the default role installation settings in Windows Server 2012 and later versions. |
| 8531 | Unofficial | Unofficial |  |  | Windows Server Update Services over HTTPS, when using the default role installation settings in Windows Server 2012 and later versions. |
| 8580 | Unofficial | Unofficial |  |  | Freegate, an Internet anonymizer and proxy tool |
| 8601 | Unofficial | Unofficial |  |  | Wavestore VMS protocol |
| 8611-8614 | Yes | Yes |  |  | Canon BubbleJet Network Protocol |
| 8629 | Unofficial |  |  |  | Tibero database |
| 8642 | Unofficial |  |  |  | Lotus Notes Traveler auto synchronization for Windows Mobile and Nokia devices |
| 8691 | Unofficial |  |  |  | Ultra Fractal, a fractal generation and rendering software application – distributed calculations over networked computers |
| 8728 | Unofficial |  |  |  | MikroTik RouterOS API |
| 8729 | Unofficial |  |  |  | MikroTik RouterOS API-SSL |
| 8765 | Unofficial |  |  |  | Default port of a local GUN relay peer that the Internet Archive and others use as a decentralized mirror for censorship resistance. |
| 8767 |  | Unofficial |  |  | Voice channel of TeamSpeak 2, a proprietary Voice over IP protocol targeted at gamers |
| 8787 | Unofficial |  |  |  | Cloudflare Workers development default |
| 8834 | Unofficial | Unofficial |  |  | Nessus, a vulnerability scanner – remote XML-RPC web server |
| 8840 | Unofficial | Unofficial |  |  | Opera Unite, an extensible framework for web applications |
| 8880 | Yes |  |  |  | Alternate port of CDDB (Compact Disc Database) protocol, used to look up audio CD (compact disc) information over the Internet. See also port 888. |
| 8880 | Unofficial | Unofficial |  |  | IBM WebSphere Application Server SOAP connector |
| 8883 | Yes | Yes |  |  | Secure MQTT (MQTT over TLS) |
| 8887 | Unofficial | Unofficial |  |  | HyperVM over HTTP |
| 8888 | Unofficial | Unofficial |  |  | HyperVM over HTTPS |
| 8888 | Unofficial |  |  |  | Freenet web UI (localhost only) |
| 8888 | Unofficial | Unofficial |  |  | Default for IPython / Jupyter notebook dashboards |
| 8888 | Unofficial | Unofficial |  |  | MAMP |
| 8889 | Unofficial | Unofficial |  |  | MAMP |
| 8920 | Unofficial | Unofficial |  |  | Jellyfin HTTPS port |
| 8983 | Unofficial | Unofficial |  |  | Apache Solr |
| 8997 | Unofficial | Unofficial |  |  | Alternate port for I2P Monotone Proxy |
| 8998 | Unofficial | Unofficial |  |  | I2P Monotone Proxy |
| 8999 | Unofficial | Unofficial |  |  | Alternate port for I2P Monotone Proxy |
| 9000 | Unofficial |  |  |  | SonarQube Web Server |
| 9000 | Unofficial |  |  |  | ClickHouse default port |
| 9000 | Unofficial |  |  |  | DBGp |
| 9000 | Unofficial |  |  |  | SqueezeCenter web server & streaming |
| 9000 | Unofficial |  |  |  | UDPCast |
| 9000 | Unofficial |  |  |  | Play Framework web server |
| 9000 | Unofficial |  |  |  | Hadoop NameNode default port |
| 9000 | Unofficial |  |  |  | PHP-FPM default port |
| 9000 | Unofficial |  |  |  | qBittorrent's embedded torrent tracker default port |
| 9000 | Unofficial |  |  |  | Emidate |
| 9001 | Yes | Yes |  |  | ETL Service Manager |
| 9001 | Unofficial | Unofficial |  |  | Microsoft SharePoint authoring environment |
| 9001 | Unofficial | Unofficial |  |  | cisco-xremote router configuration |
| 9001 | Unofficial | Unofficial |  |  | Tor network default (ORPort) |
| 9001 | Unofficial |  |  |  | DBGp Proxy |
| 9001 | Unofficial |  |  |  | HSQLDB default port |
| 9001 | Unofficial |  |  |  | Emidate |
| 9002 | Unofficial | Unofficial |  |  | Newforma Server comms |
| 9002 | Unofficial |  |  |  | Emidate |
| 9003 | Unofficial | Unofficial |  |  | Xdebug default client port |
| 9006 | Unofficial |  |  |  | Tomcat in standalone mode |
| 9008 | Unofficial |  |  |  | Zerto VRA encrypted communications listener |
| 9030 | Unofficial |  |  |  | Tor network default (DirPort) |
| 9042 | Unofficial |  |  |  | Apache Cassandra native protocol clients |
| 9043 | Unofficial |  |  |  | WebSphere Application Server Administration Console secure |
| 9050-9051 | Unofficial |  |  |  | Tor (SOCKS-5 proxy) |
| 9060 | Unofficial |  |  |  | WebSphere Application Server Administration Console |
| 9080 | Yes | Yes |  |  | glrpc, Groove Collaboration software GLRPC |
| 9080 | Unofficial |  |  |  | WebSphere Application Server HTTP Transport (port 1) default |
| 9080 | Unofficial |  |  |  | Remote Potato by FatAttitude, Windows Media Center addon |
| 9080 | Unofficial |  |  |  | ServerWMC, Windows Media Center addon |
| 9081 | Unofficial |  |  |  | Zerto ZVM to ZVM communication |
| 9090 | Unofficial |  |  |  | Cockpit |
| 9090 | Unofficial |  |  |  | Prometheus metrics server |
| 9090 | Unofficial |  |  |  | Openfire Administration console |
| 9090 | Unofficial |  |  |  | SqueezeCenter control (CLI) |
| 9090 | Unofficial |  |  |  | Cherokee Admin panel |
| 9091 | Unofficial |  |  |  | Openfire Administration console (SSL secured) |
| 9091 | Unofficial |  |  |  | Transmission (BitTorrent client) Web interface |
| 9092 | Unofficial |  |  |  | H2 (DBMS) Database server |
| 9092 | Unofficial |  |  |  | Apache Kafka A Distributed Streaming Platform |
| 9095 | Unofficial |  |  |  | Networker Web user interface server |
| 9100 | Yes | Assigned |  |  | PDL Data Stream, used for printing to certain network printers |
| 9101 | Yes | Yes |  |  | Bacula Director |
| 9102 | Yes | Yes |  |  | Bacula File Daemon |
| 9103 | Yes | Yes |  |  | Bacula Storage Daemon |
| 9116 | Unofficial |  |  |  | SNMP-exporter (Prometheus) |
| 9119 | Yes | Yes |  |  | MXit Instant Messenger |
| 9150 | Unofficial |  |  |  | Tor browser |
| 9191 | Unofficial |  |  |  | Sierra Wireless Airlink |
| 9199 | Unofficial |  |  |  | Avtex LLC—qStats |
| 9200 | Unofficial |  |  |  | Elasticsearch—default Elasticsearch port |
| 9217 | Unofficial |  |  |  | iPass Platform Service |
| 9229 | Unofficial |  |  |  | NodeJS debugging default port (localhost) |
| 9293 | Unofficial |  |  |  | Sony PlayStation RemotePlay |
| 9295 | Unofficial | Unofficial |  |  | Sony PlayStation Remote Play Session creation communication port |
| 9296 |  | Unofficial |  |  | Sony PlayStation Remote Play |
| 9297 |  | Unofficial |  |  | Sony PlayStation Remote Play Video stream |
| 9300 | Unofficial |  |  |  | IBM Cognos BI |
| 9303 |  | Unofficial |  |  | D-Link Shareport Share storage and MFP printers |
| 9306 | Yes |  |  |  | Sphinx Native API |
| 9309 | Unofficial | Unofficial |  |  | Sony PlayStation Vita Host Collaboration WiFi Data Transfer |
| 9312 | Yes |  |  |  | Sphinx SphinxQL |
| 9332 | Unofficial |  |  |  | Litecoin JSON-RPC server |
| 9333 | Unofficial |  |  |  | Litecoin |
| 9339 | Unofficial |  |  |  | Used by all Supercell games such as Brawl Stars and Clash of Clans, mobile freemium strategy video games |
| 9389 | Yes | Yes |  |  | adws, Microsoft AD DS Web Services, Powershell uses this port |
| 9392 | Unofficial |  |  |  | OpenVAS Greenbone Security Assistant web interface |
| 9418 | Yes | Yes |  |  | git, Git pack transfer service |
| 9419 | Unofficial |  |  |  | MooseFS distributed file system – master control port |
| 9420 | Unofficial |  |  |  | MooseFS distributed file system – master command port |
| 9421 | Unofficial |  |  |  | MooseFS distributed file system – master client port |
| 9422 | Unofficial |  |  |  | MooseFS distributed file system – Chunkservers |
| 9425 | Unofficial |  |  |  | MooseFS distributed file system – CGI server |
| 9443 | Unofficial |  |  |  | VMware Websense Triton console (HTTPS port used for accessing and administrating a vCenter Server via the Web Management Interface) |
| 9443 | Unofficial |  |  |  | NCSA Brown Dog Data Tilling Service |
| 9535 | Yes | Yes |  |  | mngsuite, LANDesk Management Suite Remote Control |
| 9536 | Yes | Yes |  |  | laes-bf, IP Fabrics Surveillance buffering function |
| 9600 |  | Unofficial |  |  | Factory Interface Network Service (FINS), a network protocol used by Omron programmable logic controllers |
| 9669 | Unofficial |  |  |  | VGG Image Search Engine VISE |
| 9675-9676 | Unofficial | Unofficial |  |  | Spiceworks Desktop, IT Helpdesk Software |
| 9695 | Yes | Yes |  |  | Content centric networking (CCN, CCNx) |
| 9735 | Unofficial |  |  |  | Bitcoin Lightning Network |
| 9785 | Unofficial | Unofficial |  |  | Viber |
| 9800 | Yes | Yes |  |  | WebDAV Source |
| 9800 | Unofficial | Unofficial |  |  | WebCT e-learning portal |
| 9875 | Unofficial |  |  |  | Club Penguin Disney online game for kids |
| 9876 |  | Unofficial |  |  | V Rising Dedicated server |
| 9877 | Unofficial |  |  |  | V Rising Dedicated server |
| 9898 | Unofficial |  |  |  | Tripwire—File Integrity Monitoring Software |
| 9899 |  | Yes |  |  | SCTP tunneling (port number used in SCTP packets encapsulated in UDP, RFC 6951) |
| 9901 | Unofficial |  |  |  | Banana for Apache Solr |
| 9911 | Unofficial |  |  |  | Curecoin |
| 9981 | Unofficial |  |  |  | Tvheadend HTTP server (web interface) |
| 9982 | Unofficial |  |  |  | Tvheadend HTSP server (Streaming protocol) |
| 9987 | Unofficial |  |  |  | TeamSpeak 3 server default (voice) port (for the conflicting service see the IANA list) |
| 9993 |  | Unofficial |  |  | ZeroTier Default port for ZeroTier |
| 9997 | Unofficial |  |  |  | Splunk port for communication between the forwarders and indexers |
| 9999 | Unofficial | Unofficial |  |  | Urchin Web Analytics |
| 9999 | Unofficial |  |  |  | Dash (cryptocurrency) |
| 10000 | Yes | Yes |  |  | Network Data Management Protocol (NDMP) Control stream for network backup and restore. |
| 10000 | Unofficial | Unofficial |  |  | BackupExec |
| 10000 | Unofficial | Unofficial |  |  | Webmin, Web-based Unix/Linux system administration tool (default port) |
| 10000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10001 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10001 |  | Unofficial |  |  | Ubiquiti UniFi access points broadcast to 255.255.255.255:10001 (UDP) to locate the controller(s) |
| 10002-10008 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10009 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10009 | Unofficial | Unofficial |  |  | Crossfire, a multiplayer online First Person Shooter |
| 10010 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10011 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10011 | Unofficial |  |  |  | TeamSpeak 3 ServerQuery |
| 10012-10021 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10022 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10022 | Unofficial |  |  |  | TeamSpeak 3 ServerQuery over SSH |
| 10023 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10024 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10024 | Unofficial |  |  |  | Zimbra smtp [mta]—to amavis from postfix |
| 10025 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10025 | Unofficial |  |  |  | Zimbra smtp [mta]—back to postfix from amavis |
| 10026-10041 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10042 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10042 | Unofficial |  |  |  | Mathoid server |
| 10043-10049 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10050 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10050 | Yes | Yes |  |  | Zabbix agent |
| 10051 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10051 | Yes | Yes |  |  | Zabbix trapper |
| 10052-10100 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10101 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10101 | Unofficial | Unofficial | Unofficial | Unofficial | arx Compressed file transfer protocol. |
| 10102-10109 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10110 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10110 | Yes | Yes |  |  | NMEA 0183 Navigational Data. Transport of NMEA 0183 sentences over TCP or UDP |
| 10111-10171 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10172 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10172 | Unofficial |  |  |  | Intuit Quickbooks client |
| 10173-10199 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10200 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10200 | Unofficial |  |  |  | FRISK Software International's fpscand virus scanning daemon for Unix platforms |
| 10200 | Unofficial |  |  |  | FRISK Software International's f-protd virus scanning daemon for Unix platforms |
| 10201-10204 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10201-10204 | Unofficial |  |  |  | FRISK Software International's f-protd virus scanning daemon for Unix platforms |
| 10205-10211 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10212 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10212 | Yes |  |  |  | GE Intelligent Platforms Proficy HMI/SCADA – CIMPLICITY WebView |
| 10213-10307 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10308 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10308 | Unofficial | Unofficial |  |  | Digital Combat Simulator Dedicated Server |
| 10309-10345 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10346 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10346 |  |  |  |  | TEKWorx Limited – interfaceIT board protocol |
| 10347-10467 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10468 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10468 |  | Unofficial |  |  | Flyer – discovery protocol |
| 10469-10479 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10480 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10480 | Unofficial | Unofficial |  |  | SWAT 4 Dedicated Server |
| 10481-10504 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10505 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10505 |  | Unofficial |  |  | BlueStacks (android simulator) broadcast |
| 10506-10513 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10514 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10514 | Unofficial | Unofficial |  |  | TLS-enabled Rsyslog (default by convention) |
| 10515-10577 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10578 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10578 | Unofficial |  |  |  | Skyrim Together multiplayer server for The Elder Scrolls V: Skyrim mod. |
| 10579-10799 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10800 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10800 | Unofficial |  |  |  | Touhou versus games (Immaterial and Missing Power, Phantasmagoria of Flower View, Scarlet Weather Rhapsody, Hisoutensoku, Hopeless Masquerade and Urban Legend in Limbo) |
| 10801 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10801 |  | Unofficial |  |  | Bag With Friends multiplayer server for the Peaks of Yore mod. |
| 10802-10822 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10823 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10823 |  | Unofficial |  |  | Farming Simulator 2025 |
| 10824-10890 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10891 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10891 | Unofficial |  |  |  | Jungle Disk (this port is opened by the Jungle Disk Monitor service on the localhost) |
| 10892-10932 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10933 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 10933 | Yes |  |  |  | Octopus Deploy Tentacle deployment agent |
| 10934-10999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11000 |  | Unofficial |  |  | University of Utah CS3500 Software Software Practice |
| 11001-11099 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11100 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11100 |  | Unofficial |  |  | Risk of Rain multiplayer server |
| 11101-11110 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11111 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11111 | Unofficial |  |  |  | RiCcI, Remote Configuration Interface (Redhat Linux) |
| 11112 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11112 | Yes | Yes |  |  | ACR/NEMA Digital Imaging and Communications in Medicine (DICOM) |
| 11113-11210 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11211 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11211 | Unofficial | Unofficial |  |  | memcached |
| 11212-11213 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11214 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11214 | Unofficial | Unofficial |  |  | memcached incoming SSL proxy |
| 11215 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11215 | Unofficial | Unofficial |  |  | memcached internal outgoing SSL proxy |
| 11216-11234 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11235 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11235 | Yes | Yes | Yes |  | XCOMPUTE numerical systems messaging (Xplicit Computing) |
| 11236-11310 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11311 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11311 | Unofficial | Unofficial |  |  | Robot Operating System master |
| 11312-11370 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11371 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11371 | Yes | Yes |  |  | OpenPGP HTTP key server |
| 11372-11433 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11434 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11434 | Unofficial | Unofficial |  |  | Ollama to run LLM locally |
| 11435-11752 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11753 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 11753 | Unofficial |  |  |  | OpenRCT2 multiplayer |
| 11754-11999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12000 | Unofficial | Unofficial |  |  | CubeForm, Multiplayer SandBox Game |
| 12001-12011 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12012 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12012 |  | Unofficial |  |  | Audition Online Dance Battle, Korea Server—Status/Version Check |
| 12013 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12013 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, Korea Server |
| 12014-12034 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12035 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12035 |  | Unofficial |  |  | Second Life, used for server UDP in-bound |
| 12036-12042 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12043 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12043 | Unofficial |  |  |  | Second Life, used for LSL HTTPS in-bound |
| 12044-12045 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12046 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12046 | Unofficial |  |  |  | Second Life, used for LSL HTTP in-bound<ref name="wiki.secondlife.com/wiki/LSL_HTTP_server@Functions"/> |
| 12047-12200 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12201 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12201 | Unofficial | Unofficial |  |  | Graylog Extended Log Format (GELF) |
| 12202-12221 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12222 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12222 |  | Yes |  |  | Light Weight Access Point Protocol (LWAPP) LWAPP data (RFC 5412) |
| 12223 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12223 |  | Yes |  |  | Light Weight Access Point Protocol (LWAPP) LWAPP control (RFC 5412) |
| 12224-12306 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12307 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12307 |  | Unofficial |  |  | Makerbot UDP Broadcast (client to printer) (JSON-RPC) |
| 12308 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12308 |  | Unofficial |  |  | Makerbot UDP Broadcast (printer to client) (JSON-RPC) |
| 12309-12344 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12345 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12345 | Unofficial | Unofficial |  |  | Cube World |
| 12345 | Unofficial |  |  |  | Little Fighter 2 |
| 12345 | Unofficial | Unofficial |  |  | NetBus remote administration tool (often Trojan horse). |
| 12346-12442 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12443 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12443 | Unofficial |  |  |  | IBM HMC web browser management access over HTTPS instead of default port 443 |
| 12444-12488 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12489 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12489 | Unofficial |  |  |  | NSClient/NSClient++/NC_Net (Nagios) |
| 12490-12974 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12975 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 12975 | Unofficial |  |  |  | LogMeIn Hamachi (VPN tunnel software; also port 32976)—used to connect to Mediation Server (bibi.hamachi.cc); will attempt to use SSL (TCP port 443) if both 12975 & 32976 fail to connect |
| 12976-12999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13000-13007 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13000-13007 |  | Unofficial |  |  | Second Life, used for server UDP in-bound |
| 13008 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13008 |  | Unofficial |  |  | Second Life, used for server UDP in-bound |
| 13008 | Unofficial | Unofficial |  |  | Crossfire, a multiplayer online First Person Shooter |
| 13009-13050 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13009-13050 |  | Unofficial |  |  | Second Life, used for server UDP in-bound |
| 13051-13074 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13075 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13075 | Yes |  |  |  | Default for BMC Software Control-M/Enterprise Manager Corba communication, though often changed during installation |
| 13076-13399 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13400 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13400 | Yes | Yes |  |  | ISO 13400 Road vehicles — Diagnostic communication over Internet Protocol (DoIP) |
| 13401-13719 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13720 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13720 | Yes | Yes |  |  | Symantec NetBackup—bprd (formerly VERITAS) |
| 13721 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13721 | Yes | Yes |  |  | Symantec NetBackup—bpdbm (formerly VERITAS) |
| 13722-13723 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13724 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13724 | Yes | Yes |  |  | Symantec Network Utility—vnetd (formerly VERITAS) |
| 13725-13781 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13782 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13782 | Yes | Yes |  |  | Symantec NetBackup—bpcd (formerly VERITAS) |
| 13783 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13783 | Yes | Yes |  |  | Symantec VOPIED protocol (formerly VERITAS) |
| 13784 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13785 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13785 | Yes | Yes |  |  | Symantec NetBackup Database—nbdb (formerly VERITAS) |
| 13786 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 13786 | Yes | Yes |  |  | Symantec nomdb (formerly VERITAS) |
| 13787-14549 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14550 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14550 |  | Unofficial |  |  | MAVLink Ground Station Port |
| 14551-14566 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14567 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14567 |  | Unofficial |  |  | Battlefield 1942 and mods |
| 14568-14651 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14652 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14652 | Unofficial |  |  |  | Repgen DoxBox reporting tool |
| 14653-14799 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14800 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 14800 | Unofficial |  |  |  | Age of Wonders III p2p port |
| 14801-14999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15000 | Unofficial |  |  |  | psyBNC |
| 15000 | Unofficial |  |  |  | Wesnoth |
| 15000 | Unofficial |  |  |  | Kaspersky Network Agent |
| 15000 | Unofficial |  |  |  | Teltonika networks remote management system (RMS) |
| 15001-15008 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15009-15010 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15009-15010 | Unofficial | Unofficial |  |  | Teltonika networks remote management system (RMS) |
| 15011-15344 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15345 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15345 | Yes | Yes |  |  | XPilot Contact |
| 15346-15440 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15441 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15441 | Unofficial | Unofficial |  |  | ZeroNet fileserver |
| 15442-15566 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15567 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15567 |  | Unofficial |  |  | Battlefield Vietnam and mods |
| 15568-15671 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15672 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 15672 | Unofficial |  |  |  | RabbitMQ management plugin |
| 15673-15999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16000 | Unofficial |  |  |  | Oracle WebCenter Content: Imaging (formerly known as Oracle Universal Content Management). Port though often changed during installation |
| 16000 | Unofficial |  |  |  | shroudBNC |
| 16001-16079 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16080 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16080 | Unofficial |  |  |  | macOS Server Web (HTTP) service with performance cache |
| 16081-16199 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16200 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16200 | Unofficial |  |  |  | Oracle WebCenter Content: Content Server (formerly known as Oracle Universal Content Management). Port though often changed during installation |
| 16201-16224 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16225 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16225 | Unofficial |  |  |  | Oracle WebCenter Content: Content Server Web UI. Port though often changed during installation |
| 16226-16249 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16250 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16250 | Unofficial |  |  |  | Oracle WebCenter Content: Inbound Refinery (formerly known as Oracle Universal Content Management). Port though often changed during installation |
| 16251-16260 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16261 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16261 | Unofficial | Unofficial |  |  | Project Zomboid multiplayer. Additional sequential ports used for each player connecting to server. |
| 16262-16299 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16300 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16300 | Unofficial |  |  |  | Oracle WebCenter Content: Records Management (formerly known as Oracle Universal Records Management). Port though often changed during installation |
| 16301-16378 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16379 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16379 | Unofficial |  |  |  | Redis Cluster bus |
| 16380-16383 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16384 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16384 |  | Unofficial |  |  | CISCO Default RTP MIN |
| 16384 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16384 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's FaceTime and Game Center |
| 16385-16387 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16385-16387 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16385-16387 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's FaceTime and Game Center |
| 16388-16392 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16388-16392 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16393-16399 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16393-16399 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16393-16399 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's FaceTime and Game Center |
| 16400 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16400 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16400 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's FaceTime and Game Center |
| 16400 | Unofficial |  |  |  | Oracle WebCenter Content: Capture (formerly known as Oracle Document Capture). Port though often changed during installation |
| 16401-16402 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16401-16402 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16401-16402 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's FaceTime and Game Center |
| 16403 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16403 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's iChat for audio and video |
| 16403 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's Game Center |
| 16404-16472 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16404-16472 |  | Unofficial |  |  | Real-time Transport Protocol (RTP), RTP Control Protocol (RTCP), used by Apple's Game Center |
| 16473-16566 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16567 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 16567 |  | Unofficial |  |  | Battlefield 2 and mods |
| 16568-16999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17000 |  | Unofficial |  |  | M17 – Digital RF voice and data protocol with Internet (UDP) gateways (reflectors). |
| 17001-17010 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17011 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17011 | Unofficial |  |  |  | Worms multiplayer |
| 17012-17223 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17224 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17224 | Yes | Yes |  |  | Train Realtime Data Protocol (TRDP) Process Data, network protocol used in train communication. |
| 17225 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17225 | Yes | Yes |  |  | Train Realtime Data Protocol (TRDP) Message Data, network protocol used in train communication. |
| 17226-17332 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17333 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17333 | Unofficial |  |  |  | CS Server (CSMS), default binary protocol port |
| 17334-17471 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17472 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17472 |  |  |  |  | Tanium Communication Port |
| 17473 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17474 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17474 |  | Unofficial |  |  | DMXControl 3 Network Discovery |
| 17475 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17475 | Unofficial |  |  |  | DMXControl 3 Network Broker |
| 17476 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17476 | Unofficial |  |  |  | DMXControl 3 Network Broker TLS |
| 17477-17499 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17500 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 17500 | Yes | Yes |  |  | Dropbox LanSync Protocol (db-lsp); used to synchronize file catalogs between Dropbox clients on a local network. |
| 17501-18079 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18080 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18080 | Unofficial |  |  |  | Monero P2P network communications |
| 18081 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18081 | Unofficial |  |  |  | Monero incoming RPC calls |
| 18082-18090 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18091 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18091 | Unofficial | Unofficial |  |  | memcached Internal REST HTTPS for SSL |
| 18092 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18092 | Unofficial | Unofficial |  |  | memcached Internal CAPI HTTPS for SSL |
| 18093-18103 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18104 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18104 | Yes |  |  |  | RAD PDF Service |
| 18105-18199 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18200 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18200 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, AsiaSoft Thailand Server status/version check |
| 18201 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18201 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, AsiaSoft Thailand Server |
| 18202-18205 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18206 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18206 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, AsiaSoft Thailand Server FAM database |
| 18207-18299 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18300 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18300 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, AsiaSoft SEA Server status/version check |
| 18301 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18301 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, AsiaSoft SEA Server |
| 18302-18305 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18306 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18306 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, AsiaSoft SEA Server FAM database |
| 18307-18332 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18333 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18333 | Unofficial |  |  |  | Bitcoin testnet |
| 18334-18399 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18400 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18400 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, KAIZEN Brazil Server status/version check |
| 18401 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18401 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, KAIZEN Brazil Server |
| 18402-18504 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18505 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18505 | Unofficial | Unofficial |  |  | Audition Online Dance Battle R4p3 Server, Nexon Server status/version check |
| 18506 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18506 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, Nexon Server |
| 18507-18604 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18605 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18605 | Unofficial | Unofficial |  |  | X-BEAT status/version check |
| 18606 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18606 | Unofficial | Unofficial |  |  | X-BEAT |
| 18607-18675 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18676 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18676 | Unofficial | Unofficial |  |  | YouView |
| 18677-18768 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18769 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 18769 | Yes | Yes |  |  | iQue Protocol |
| 18770-18999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19000 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, G10/alaplaya Server status/version check |
| 19000 | Unofficial |  |  |  | JACK sound server |
| 19001 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19001 | Unofficial | Unofficial |  |  | Audition Online Dance Battle, G10/alaplaya Server |
| 19002-19131 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19132 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19132 |  | Unofficial |  |  | Minecraft: Bedrock Edition multiplayer server |
| 19133 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19133 |  | Unofficial |  |  | Minecraft: Bedrock Edition IPv6 multiplayer server |
| 19134-19149 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19150 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19150 | Unofficial | Unofficial |  |  | Gkrellm Server |
| 19151-19225 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19226 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19226 | Unofficial |  |  |  | Panda Software AdminSecure Communication Agent |
| 19227-19293 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19294 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19294 | Unofficial |  |  |  | Google Talk Voice and Video connections |
| 19295 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19295 |  | Unofficial |  |  | Google Talk Voice and Video connections |
| 19296-19301 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19302 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19302 |  | Unofficial |  |  | Google Talk Voice and Video connections |
| 19303-19530 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19531 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19531 | Unofficial |  |  |  | systemd-journal-gatewayd |
| 19532 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19532 | Unofficial |  |  |  | systemd-journal-remote |
| 19533-19770 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19771 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19771 | Unofficial |  |  |  | Softros LAN Messenger uses TCP and UDP ports for collecting user lists and sending messages |
| 19772-19787 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19788 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19788 |  | Yes |  |  | Mesh Link Establishment protocol for IEEE 802.15.4 radio mesh networks |
| 19789-19811 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19812 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19812 | Yes |  |  |  | 4D database SQL Communication |
| 19813 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19813 | Yes | Yes |  |  | 4D database Client Server Communication |
| 19814 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19814 | Yes |  |  |  | 4D database DB4D Communication |
| 19815-19879 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19880 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19880 | Unofficial |  |  |  | Softros LAN Messenger uses TCP port for file transfers |
| 19881-19998 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19999 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 19999 | Yes | Yes |  |  | Distributed Network Protocol—Secure (DNP—Secure), a secure version of the protocol used in SCADA systems between communicating RTU's and IED's |
| 20000 |  | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 20000 | Yes | Yes |  |  | Distributed Network Protocol (DNP), a protocol used in SCADA systems between communicating RTU's and IED's |
| 20000 | Yes | Yes |  |  | OpenWebNet, communications protocol used in Bticino products |
| 20000 | Unofficial | Unofficial |  |  | Usermin, Web-based Unix/Linux user administration tool (default port) |
| 20000 | Unofficial | Unofficial |  |  | Used on VoIP networks for receiving and transmitting voice telephony traffic which includes Google Voice via the OBiTalk ATA devices as well as on the MagicJack and Vonage ATA network devices. |
| 20560 | Unofficial | Unofficial |  |  | Killing Floor |
| 20580-20581 | Unofficial | Unofficial |  |  | Walljam device communications |
| 20595 |  | Unofficial |  |  | 0 A.D. Empires Ascendant |
| 20808 |  | Unofficial |  |  | Ableton Link |
| 21025 | Unofficial |  |  |  | Starbound Server (default), Starbound |
| 21064 | Unofficial |  |  |  | Default Ingres DBMS server |
| 22000 | Unofficial |  |  |  | Syncthing (default) |
| 22067 | Unofficial |  |  |  | [https://docs.syncthing.net/users/strelaysrv.html Syncthing Relay Server] (strelaysrv) |
| 22070 | Unofficial |  |  |  | Syncthing Relay Server (strelaysrv) - Status service |
| 22136 | Unofficial |  |  |  | FLIR Systems Camera Resource Protocol |
| 22222 | Unofficial |  |  |  | Davis Instruments, WeatherLink IP |
| 22347 | Yes | Yes |  |  | WibuKey, WIBU-SYSTEMS AG Copy protection |
| 22350 | Yes | Yes |  |  | CodeMeter, WIBU-SYSTEMS AG Copy protection |
| 22351 | Yes |  |  |  | CodeMeter-CmWAN, WIBU-SYSTEMS AG Copy protection |
| 23073 | Unofficial | Unofficial |  |  | Soldat Dedicated Server |
| 23399 | Unofficial | Unofficial |  |  | Skype default protocol |
| 23513 | Unofficial | Unofficial |  |  | Duke Nukem 3D source ports |
| 24441 | Unofficial | Unofficial |  |  | Pyzor spam detection network |
| 24444 | Unofficial | Unofficial |  |  | NetBeans integrated development environment |
| 24454 |  | Unofficial |  |  | Minecraft (Java Edition) Simple Voice Chat mod voice server |
| 24465 | Yes | Yes |  |  | Tonido Directory Server for Tonido which is a Personal Web App and P2P platform |
| 24554 | Yes | Yes |  |  | BINKP, Fidonet mail transfers over TCP/IP |
| 24800 | Unofficial | Unofficial |  |  | Synergy: keyboard/mouse sharing software |
| 24842 | Unofficial | Unofficial |  |  | StepMania: Online: Dance Dance Revolution Simulator |
| 25565 | Unofficial |  |  |  | Minecraft (Java Edition) multiplayer server |
| 25565 | Unofficial |  |  |  | Minecraft (Java Edition) multiplayer server query |
| 25575 | Unofficial |  |  |  | Minecraft (Java Edition) multiplayer server |
| 25585 | Unofficial |  |  |  | Minecraft (Java Edition) multiplayer server management |
| 25734-25735 | Unofficial | Unofficial |  |  | SolidWorks SolidNetworkLicense Manager |
| 25826 |  | Unofficial |  |  | collectd default port |
| 26000 | Yes | Yes |  |  | id Software's Quake server |
| 26000 | Unofficial |  |  |  | EVE Online, iVentoy webGUI (see Ventoy) |
| 26000 | Unofficial |  |  |  | Xonotic, an open-source arena shooter |
| 26822 |  | Unofficial |  |  | MSI MysticLight |
| 26900-26901 | Unofficial |  |  |  | EVE Online |
| 26909-26911 | Unofficial |  |  |  | Action Tanks Online |
| 27000 | Unofficial |  |  |  | PowerBuilder SySAM license server |
| 27000 |  | Unofficial |  |  | id Software's QuakeWorld master server |
| 27000 | Yes | Yes |  |  | FlexNet Publisher's License server (from the range of default ports) |
| 27000 |  | Unofficial |  |  | Steam (game client traffic) |
| 27001-27006 |  | Unofficial |  |  | id Software's QuakeWorld master server |
| 27001-27006 | Yes | Yes |  |  | FlexNet Publisher's License server (from the range of default ports) |
| 27001-27006 |  | Unofficial |  |  | Steam (game client traffic) |
| 27007-27009 | Yes | Yes |  |  | FlexNet Publisher's License server (from the range of default ports) |
| 27007-27009 |  | Unofficial |  |  | Steam (game client traffic) |
| 27010-27014 |  | Unofficial |  |  | Steam (game client traffic) |
| 27015 |  | Unofficial |  |  | Steam (game client traffic) |
| 27015 |  | Unofficial |  |  | GoldSrc, Source engine and Source 2 engine dedicated server port |
| 27015 |  | Unofficial |  |  | Unturned, a survival game |
| 27015 |  | Unofficial |  |  | Steam (matchmaking and HLTV) |
| 27015 | Unofficial | Unofficial |  |  | Steam (downloads) |
| 27016 |  | Unofficial |  |  | Unturned, a survival game |
| 27016 |  | Unofficial |  |  | Steam (matchmaking and HLTV) |
| 27016 | Unofficial | Unofficial |  |  | Steam (downloads) |
| 27016 | Unofficial | Unofficial |  |  | Magicka and Space Engineers server port |
| 27017 |  | Unofficial |  |  | Unturned, a survival game |
| 27017 |  | Unofficial |  |  | Steam (matchmaking and HLTV) |
| 27017 | Unofficial | Unofficial |  |  | Steam (downloads) |
| 27017 | Unofficial |  |  |  | MongoDB daemon process (<code>mongod</code>) and routing service (<code>mongos</code>) |
| 27018 |  | Unofficial |  |  | Unturned, a survival game |
| 27018 |  | Unofficial |  |  | Steam (matchmaking and HLTV) |
| 27018 | Unofficial | Unofficial |  |  | Steam (downloads) |
| 27019-27030 |  | Unofficial |  |  | Steam (matchmaking and HLTV) |
| 27019-27030 | Unofficial | Unofficial |  |  | Steam (downloads) |
| 27031-27035 |  | Unofficial |  |  | Steam (In-Home Streaming) |
| 27036 | Unofficial | Unofficial |  |  | Steam (In-Home Streaming) |
| 27100 | Unofficial | Unofficial |  |  | Screen Play Games controller |
| 27374 | Unofficial | Unofficial |  |  | Sub7 default. |
| 27500-27887 |  | Unofficial |  |  | id Software's QuakeWorld |
| 27888 |  | Unofficial |  |  | id Software's QuakeWorld |
| 27888 |  | Unofficial |  |  | Kaillera server |
| 27889-27900 |  | Unofficial |  |  | id Software's QuakeWorld |
| 27901-27910 |  | Unofficial |  |  | id Software's Quake II master server |
| 27950 |  | Unofficial |  |  | OpenArena outgoing |
| 27960-27969 |  | Unofficial |  |  | Activision's Enemy Territory and id Software's Quake III Arena, Quake III and Quake Live and some ioquake3 derived games, such as Urban Terror (OpenArena incoming) |
| 28000 | Yes | Yes |  |  | Siemens Digital Industries Software license server |
| 28001 | Unofficial | Unofficial |  |  | Starsiege: Tribes |
| 28015-28016 |  | Unofficial |  |  | Rust (video game) |
| 28200 | Assigned | Assigned |  |  | VoxelStorm game server |
| 28260 | Unofficial |  |  |  | Palo Alto Networks' Panorama HA-1 backup unencrypted sync port. |
| 28443 | Unofficial |  |  |  | Palo Alto Networks' Panorama-to-managed devices software updates, PAN-OS 8.0 and later. |
| 28769 | Unofficial |  |  |  | Palo Alto Networks' Panorama HA unencrypted sync port. |
| 28770 | Unofficial |  |  |  | Palo Alto Networks' Panorama HA-1 backup sync port. |
| 28770 |  | Unofficial |  |  | AssaultCube Reloaded, a video game based upon a modification of AssaultCube |
| 28771 |  | Unofficial |  |  | AssaultCube Reloaded, a video game based upon a modification of AssaultCube |
| 28785-28786 |  | Unofficial |  |  | Cube 2: Sauerbraten |
| 28852 | Unofficial | Unofficial |  |  | Killing Floor |
| 28910 | Unofficial | Unofficial |  |  | Nintendo Wi-Fi Connection |
| 28960 | Unofficial | Unofficial |  |  | Call of Duty: World at War (PC platform) |
| 29000 | Yes | Yes |  |  | Siemens Digital Industries Software license server |
| 29070 | Unofficial | Unofficial |  |  | Jedi Knight: Jedi Academy by Ravensoft |
| 29900-29901 | Unofficial | Unofficial |  |  | Nintendo Wi-Fi Connection |
| 29920 | Unofficial | Unofficial |  |  | Nintendo Wi-Fi Connection |
| 30000 | Unofficial |  |  |  | XLink Kai P2P |
| 30000 | Unofficial |  |  |  | Luanti server default port |
| 30000 | Unofficial |  |  |  | Foundry Virtual Tabletop server default port |
| 30003 |  |  |  |  | Amicon FPSU-IP Remote Administration |
| 30004 |  |  |  |  | Amicon FPSU-IP VPN |
| 30033 | Unofficial |  |  |  | TeamSpeak 3 File Transfer |
| 30120 | Unofficial | Unofficial |  |  | Fivem (Default Port) GTA V multiplayer |
| 30564 | Unofficial |  |  |  | Multiplicity: keyboard/mouse/clipboard sharing software |
| 30814 | Unofficial | Unofficial |  |  | [https://beammp.com/ BeamMP]: Unofficial BeamNG.drive multiplayer mod. Default server port |
| 31337 | Unofficial |  |  |  | Back Orifice and Back Orifice 2000 remote administration tools |
| 31337 | Unofficial | Unofficial |  |  | ncat, a netcat alternative |
| 31416 | Unofficial | Unofficial |  |  | BOINC RPC |
| 31438 | Unofficial |  |  |  | Rocket U2 |
| 31457 | Yes |  |  |  | TetriNET |
| 32137 | Unofficial | Unofficial |  |  | Immunet Protect (UDP in version 2.0, TCP since version 3.0) |
| 32400 | Yes |  |  |  | Plex Media Server |
| 32749 | Unofficial |  |  |  | Gridcoin |
| 32764 | Unofficial |  |  |  | A backdoor found on certain Linksys, Netgear and other wireless DSL modems/combination routers |
| 32887 |  | Unofficial |  |  | Ace of Spades, a multiplayer FPS video game |
| 32976 | Unofficial |  |  |  | LogMeIn Hamachi, a VPN application; also TCP port 12975 and SSL (TCP 443). |
| 33434 | Yes | Yes |  |  | traceroute |
| 33848 |  | Unofficial |  |  | Jenkins, a continuous integration (<abbr>CI</abbr>) tool |
| 34000 |  | Unofficial |  |  | Infestation: Survivor Stories (formerly known as The War Z), a multiplayer zombie video game |
| 34197 |  | Unofficial |  |  | Factorio, a multiplayer survival and factory-building game |
| 35357 | Yes |  |  |  | OpenStack Identity (Keystone) administration |
| 36330 | Unofficial |  |  |  | Folding@home Control Port |
| 37008 |  | Unofficial |  |  | TZSP intrusion detection |
| 38412 |  |  | Yes |  | NG Application Protocol (NGAP) for communication between a gNB and AMF in 5G core networks |
| 40000 | Yes | Yes |  |  | SafetyNET p – a real-time Industrial Ethernet protocol |
| 41121 | Yes | Reserved |  |  | Tentacle Server – Pandora FMS |
| 41230 | Assigned | Yes |  |  | Z-Wave Protocol over DTLS |
| 41794 | Yes | Yes |  |  | Crestron Control Port – Crestron Electronics |
| 41795 | Yes | Yes |  |  | Crestron Terminal Port – Crestron Electronics |
| 41796 | Yes |  |  |  | Crestron Secure Control Port – Crestron Electronics |
| 41797 | Yes |  |  |  | Crestron Secure Terminal Port – Crestron Electronics |
| 42081-42090 | Yes | Yes |  |  | Zippin –Zippin Store |
| 42420 | Unofficial | Unofficial |  |  | Vintage Story multiplayer server |
| 42590-42595 | Yes | Yes |  |  | Glue – MakePro X |
| 42999 |  |  |  |  | [https://curiosity.ai/ Curiosity] |
| 43110 | Unofficial |  |  |  | ZeroNet web UI default port |
| 43594-43595 | Unofficial | Unofficial |  |  | RuneScape |
| 44123 | Assigned | Unofficial |  |  | Z-Wave Secure Tunnel |
| 44405 | Unofficial |  |  |  | Mu Online Connect Server |
| 44818 | Yes | Yes |  |  | EtherNet/IP explicit messaging |
| 47808-47823 | Yes | Yes |  |  | BACnet Building Automation and Control Networks (47808<sub>10</sub> = BAC0<sub>16</sub> to 47823<sub>10</sub> = BACF<sub>16</sub>) |
| 48556 | Yes | Yes |  |  | drive.web AC/DC Drive Automation and Control Networks |
| 48656 | Unofficial |  |  |  | Brainy LAB Control Server |
| 48657 |  | Unofficial |  |  | Brainy LAB Control Server |
| 49151 | Reserved | Reserved |  |  | "IANA Reserved" } |
| 49152-49159 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 49160 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 49160 | Unofficial |  |  |  | Palo Alto Networks' Panorama. |
| 49161-50159 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 50160 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 50160 |  |  |  |  | colspan="2" S-CONNECT protocol - data exchange (TCP) and manual device pairing (UDP). |
| 50161 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 50161 |  |  |  |  | S-CONNECT protocol - automatic device pairing. |
| 50162-51412 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 51413 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 51413 | Unofficial |  |  |  | Transmission (BitTorrent client) |
| 51414-51514 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 51515 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 51515 | Unofficial |  |  |  | [https://kopia.io/ Kopia] server |
| 51516-51819 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 51820 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 51820 |  | Unofficial |  |  | WireGuard protocol |
| 51821-52379 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 52380 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 52380 |  | Unofficial |  |  | Sony VISCA Network Setting Protocol |
| 52381 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 52381 |  | Unofficial |  |  | Sony VISCA over IP Protocol |
| 52382-53316 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 53317 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 53317 | Unofficial |  |  |  | LocalSend |
| 53318-59099 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 59100 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 59100 | Unofficial | Unofficial |  |  | AudioRelay |
| 59101-59999 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 60000-61000 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 60000-61000 |  | Unofficial |  |  | Range from which Mosh – a remote-terminal application similar to SSH – typically assigns ports for ongoing sessions between Mosh servers and Mosh clients. |
| 61001-61615 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 61616 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 61616 | Unofficial |  |  |  |  |
| 61617-62077 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 62078 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 62078 | Unofficial |  |  |  |  |
| 62079-64737 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 64738 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
| 64738 | Unofficial | Unofficial |  |  | Mumble } |
| 64739-65535 | Unofficial |  |  |  | Certificate Management over CMS and Xsan Filesystem Access |
