# Mission 7 — How computers communicate

## 1. Task / objective
The goal of this mission was to learn how computers communicate across networks. I explored fundamental networking concepts (LAN, MAN, WAN, DNS, routers, protocols, packet switching, client-server), ran terminal tests (`ping` and `nslookup`) to check connection latency and DNS resolution without exposing personal IP details, and traced the step-by-step process of what happens when a user opens a website in a browser.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A local network covering a small physical area, like one room, house, or college lab. | My home Wi-Fi connecting my laptop, phone, and printer. |
| **MAN** | A larger network connecting multiple buildings or sites across a city or campus. | A university campus network connecting all academic blocks and hostels. |
| **WAN** | A massive network that spans large geographical areas like states, countries, or the whole world. | The global Internet. |
| **DNS** | The phonebook of the internet that converts website names people remember into numeric IP addresses that computers need. | Translating `example.com` into the IP address `104.20.23.154`. |
| **Router** | A networking device that directs and forwards data packets between different networks. | The Wi-Fi router in my home connecting our devices to the internet service provider. |
| **Protocol** | An agreed set of rules that computers follow so they can understand each other and transfer data reliably. | **HTTP / HTTPS** for loading websites; **TCP** for reliable data delivery. |
| **Packet switching** | Splitting large data (like an image or webpage) into smaller chunks called packets, sending them across the network independently, and putting them back together at the destination. | Streaming a video on YouTube where data arrives in small packets continuously. |
| **Client-server** | A system where one device (the client) asks for data or a service, and another computer (the server) listens and sends back the requested data. | My laptop browser (client) requesting a web page from a web server hosting a site. |

---

### Task 7.2 — Observe network information

#### 1. Connectivity test (`ping -c 3 example.com`)
```
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=25.146 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=13.908 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=15.977 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 13.908/18.344/25.146/4.884 ms
```

#### 2. DNS lookup (`nslookup example.com`)
```
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

#### Questions and answers:
- **What does a connectivity test help you check?**  
  `ping` helps you test whether your computer can reach a remote server over the network. It tells you if the server is responding, how long it takes for a message to go and come back (round-trip time in milliseconds), and if any data packets were lost along the way (0.0% packet loss here).
- **What information does a DNS lookup display?**  
  `nslookup` shows which DNS server answered your request (`8.8.8.8`) and gives the exact IP addresses (`104.20.23.154` and `172.66.147.243`) that correspond to the domain name you looked up.
- **What is the role of DNS when you enter a website name in a browser?**  
  When you type a domain name like `example.com` into your browser, the computer doesn't know where that server lives yet. DNS looks up the domain name and returns the server's numerical IP address so your browser can connect to it.

*(Privacy note: Personal details like home Wi-Fi name and private local IP address were omitted).*

---

### Task 7.3 — What happens when you open a website?
Here is the step-by-step process in 6 steps:

1. **User types the URL in the browser (client)**:  
   You type `https://example.com` into your browser and press Enter. The browser recognizes that you want to connect using the HTTPS protocol.
2. **DNS lookup finds the server IP address**:  
   The browser checks its cache or asks a DNS server to look up `example.com`. The DNS server replies with the server's IP address (e.g., `104.20.23.154`).
3. **Establishing a connection via routers**:  
   Your computer sends data packets through your local router and across internet routers to establish a TCP and TLS encrypted connection with the server's IP address.
4. **Sending the HTTP request**:  
   Once the connection is open, your browser sends an HTTP GET request asking the web server for the website's main page.
5. **The server processes the request**:  
   The web server receives the request, locates the requested HTML file, and packages an HTTP response (with status code `200 OK`).
6. **Receiving data and rendering the webpage**:  
   The server sends the website files back in packets. Your browser receives the packets, reassembles them, parses the HTML, CSS, and images, and displays the finished page on your screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com` - Tested connection latency and packet loss.
- `nslookup example.com` - Looked up the IP address linked to the domain name.

## 4. My understanding
Before this mission, I thought typing a URL was a single direct action. Now I understand that opening a website involves multiple cooperative steps: DNS translating the human name to an IP, routers forwarding small packets across networks, TCP ensuring no packets get lost, and HTTP/HTTPS governing how the browser and server talk.

## 5. Difficulties faced
Making sure that running network commands did not leak any private Wi-Fi network names or personal local IP addresses in the assignment report.

## 6. How I resolved them
I ran `ping` and `nslookup` only against the safe public domain `example.com` and checked the terminal output to ensure no private local subnet addresses or personal network details were copied into the README.

## 7. Evidence / files
- `mission-07-networking/README.md` containing network definitions, command outputs, and the 6-step website breakdown.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Pushed to: `main` branch on GitHub.
