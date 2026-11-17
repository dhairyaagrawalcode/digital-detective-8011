# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to explore computer networking fundamentals, examine network scales and core architectural concepts (LAN, MAN, WAN, DNS, routers, protocols, packet switching, client-server models), conduct privacy-safe diagnostic network tests (`ping` and `nslookup`), and describe the step-by-step lifecycle of accessing a website over the internet.

---

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A computer network constrained to a small, localized physical area such as a single home, classroom, computer laboratory, or office building. | A home Wi-Fi network connecting a laptop, mobile phone, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A larger network infrastructure spanning an entire city or educational campus, interconnecting multiple smaller LANs. | A municipal fiber-optic network connecting city government offices, police stations, and university campus libraries. |
| **WAN (Wide Area Network)** | A network spanning vast geographical regions, countries, or across the globe, connecting millions of heterogeneous systems. | The global Internet, or an international banking network connecting branches across continents. |
| **DNS (Domain Name System)** | The distributed naming directory of the internet that translates human-friendly domain names into machine-routable numeric IP addresses. | Resolving `example.com` into destination IP addresses `104.20.23.154` and `172.66.147.243`. |
| **Router** | A specialized network layer device that connects two or more distinct networks, inspecting destination IP addresses to forward packets along the optimal route. | A home Wi-Fi broadband router connecting local residential devices to the Internet Service Provider's (ISP) network. |
| **Protocol** | A standardized set of established rules, formats, and procedures that govern how computing devices package, transmit, verify, and receive data. | **HTTP / HTTPS** for web browsing; **TCP/IP** for reliable packet transmission; **SSH** for secure remote shell access. |
| **Packet Switching** | A communication methodology where data messages are divided into discrete chunks called packets, routed independently through networks, and reassembled at the destination. | Streaming a YouTube video or downloading a file across multiple intermediate internet pathways. |
| **Client-Server** | A distributed computing architecture where a client system requests resources, files, or processing services, and a centralized server listens, processes, and fulfills the request. | A web browser (client) requesting a web page from a web server hosting `example.com`. |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test (`ping -c 3 example.com`)
```
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=25.146 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=13.908 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=15.977 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 13.908/18.344/25.146/4.884 ms
```

#### 2. DNS Lookup (`nslookup example.com`)
```
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

#### Network Questions & Analysis
- **What does a connectivity test (`ping`) help you check?**  
  A connectivity test verifies whether a target host on an IP network is reachable and measures round-trip time (latency) using ICMP echo requests. It checks network link health, transmission delays, and identifies whether data packets are being dropped (packet loss).
- **What information does a DNS lookup display?**  
  A DNS lookup reveals which DNS resolver answered the query, the port used (`#53`), and the authoritative or non-authoritative mappings linking the domain name to its corresponding IPv4 and IPv6 network addresses.
- **What is the role of DNS when entering a website name in a browser?**  
  Human users recall memorable words like `example.com`, but network routers can only route packets using numerical IP addresses. DNS acts as the essential automated directory service: the moment a URL is requested, DNS resolves the domain into the target server's exact IP address so the browser can establish a TCP/IP connection.

*(Note: In accordance with privacy rules, local private network IP addresses, Wi-Fi SSIDs, and router hardware MAC addresses have been omitted).*

---

### Task 7.3 — What happens when you open a website?

1. **User Request & URL Parsing (Client)**:  
   The user types a web address (e.g., `https://example.com`) into the web browser (the client) and presses Enter. The browser identifies the protocol (`HTTPS`), the host domain (`example.com`), and the default web port (`443`).
2. **DNS Resolution**:  
   The client checks its local cache and, if not found, dispatches a DNS query to the configured DNS recursive resolver. The DNS system looks up the root, TLD, and authoritative nameservers to resolve `example.com` to its corresponding IP address (`104.20.23.154`).
3. **Connection Handshake Across Routers**:  
   The client initiates a Transmission Control Protocol (TCP) 3-way handshake (`SYN`, `SYN-ACK`, `ACK`) followed by a TLS cryptographic handshake to establish an encrypted, reliable communication channel. Data packets are forwarded hop-by-hop across intermediate routers using packet switching.
4. **HTTP Request Transmission**:  
   Over the secured TLS connection, the client browser formats and transmits an `HTTP GET` request according to the Hypertext Transfer Protocol specifications, requesting the root webpage resource (`/`).
5. **Server Processing**:  
   The destination web server receives the HTTP request packets, parses the headers, verifies permissions, processes any dynamic server scripts or database lookups, and prepares an HTTP response package.
6. **HTTP Response & Content Rendering**:  
   The server transmits an HTTP response containing a status code (`200 OK`) and the payload (HTML, CSS, JavaScript files) broken into TCP packets. The client receives, acknowledges, and reassembles the packets, while the browser rendering engine parses the DOM, applies styles, executes scripts, and displays the interactive webpage on the screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested network connectivity, latency, and packet loss using ICMP packets.
- `nslookup example.com`: Performed DNS queries to resolve domain names to IP addresses.
- Markdown editor: Structured network analysis and workflow diagrams.

---

## 4. My understanding
Networking turns isolated computers into a collaborative worldwide web. Network architectures scale from personal LANs to global WANs through standardized protocols (TCP/IP stack). Protocols govern everything from low-level packet switching and routing across physical hardware to application-level services like DNS and HTTP. The seamless client-server model allows client devices to tap into massive cloud computing resources across the globe in milliseconds.

---

## 5. Difficulties faced
Preventing local sensitive network credentials (such as internal Gateway IPs, subnet masks, and Wi-Fi network names) from leaking into assignment logs.

---

## 6. How I resolved them
Configured network tests specifically against public domains (`example.com`) using public DNS resolvers (`8.8.8.8`) and verified all terminal outputs were sanitized and free of private network identifiers.

---

## 7. Evidence / files
- `mission-07-networking/README.md`: Documented networking concepts, `ping` and `nslookup` logs, and the 6-step website lifecycle.

---

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Status: Staged, committed, and pushed to `main` branch on GitHub.
