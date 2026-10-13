# Nornir HIVE Q&A

Older follow-up to the partner deck. Not a 2026 public page. Performance multiples in here are claims, not verified measurements. The source says a research write-up was still hoped for in May or June and was not finished in this document.

## HIVE Collective

The deck says Nornir HIVE enables two-way communication between different technology stacks and cross-domain communication. The answer in this note:

Nornir HIVE is based on a bijective architecture model invented by the founders. Three products build the stack:

- Synx BIOS: a decentralized network operating system.
- Synx C-DNS: a domain name system for the client network.
- Synx Pass: authentication and identification for ownership control.

Nornir uses these three to run the HIVE Collective as software as a service.

Originally the Synx product was meant to launch as developer tools so people could set up their own namespace and join a heterogeneous self-scaling network, the Real Time Web, for IoT and edge resources in a dynamic event-driven peer-to-peer linking network. Lack of initial funding led them to prove the technology first. That became the Nornir HIVE Collective: a private network, Real Time Web on a small scale, an intranet solution.

A heterogeneous system, in this note, is a network nobody owns, like the Web. It contrasts that with Microsoft Azure or an IoT hub controlled by one entity, and says even a blockchain is not fully heterogeneous if everyone must share one ledger.

The Real Time Web is designed to be open. You join by registering a domain and getting address space. It is backward compatible with TCP. Using Synx C-DNS to establish a domain maps the IP with the RTW domain and is described as enhancing TCP so it becomes event driven, with linked data and semantic-web topology. The communication stack is split so ownership can be controlled in each layer.

A consumer can control their data in the data layer and does not get the application layer. The service provider can configure the application layer and does not get the lower stack layers.

The Web hyperlink model here is described as unidirectional request-response, historical information. Machines, IoT, and robots are said to need bidirectional data from the source, which is why an API industry exists. This note says the RTW model replaces building an API and a server to manage connections, and uses linking plus event distribution instead. Synx tools administrate the domains.

## Energy and cost claims

Unverified. This note says they were collaborating with a research institute and hoped the paper would be finished in May or June. Do not state these multiples as facts.

The claimed contrast: traditional client data is preprogrammed to a server, which keeps session details and persists data temporarily before redistributing it, with API programming and intermediaries, and copies along the route. The bijective system uses linked data to construct the value chain in the application layer. Data sits in a separate layer and traverses only when someone is listening. Normally the same owner is on both ends. Synx Pass manages ownership changes. Transferring an instance to another user sends the data to that user.

Temperature example in this note: a traditional server stores the reading and the user polls. In HIVE the user gets an event when the temperature changes. The note says HIVE does not require a handshake or a server deployment for that case.

Experiences listed, still unverified:

- Linking between services can be altered at runtime by commands to the runtime operating system, instead of programming and maintaining an API.
- Network resources can be morphed to a local data model. The example: if your system uses Kelvin, that is what you get; if the other system uses Celsius, that is what it gets. The source spells one unit "Klevin".
- Protocol independence: the same service can be reached by HTTPS or websocket, and the client can switch at runtime.

The note says the energy claim is about how much data is distributed, and that bytes sent versus received were "close to 99.9% efficiency" because what you send is what you receive without overhead and intermediaries. Treat that figure as their claim, not a measurement in this corpus.

## Speed claim

The deck said the event-driven network is "1000 times faster." This answer walks that back. It says the assertion is mostly about complex value chains in IoT and smart buildings. For dedicated peer-to-peer between two tiers, the statement does not hold. Latency in a HIVE network is basically the ping time between two IP addresses, because Synx BIOS is in the stack and is event driven. The latency is the network lag between the IPs and the clients.

## Security and GDPR

This note says they follow best practices and that security is ongoing. They started with a proprietary security and encryption model, then chose an existing open-source tool. For the private HIVE Collective they offer Keycloak (SSO, dynamic token, two-factor, and more) as the authentication service. Combined with Synx Pass, the owner of a domain or service can add, remove, and alter ownership on network resources at runtime.

Synx Pass is described as controlling ownership in four layers, because a minimum of four entities sit in a vertical value chain: infrastructure (ISP, hardware, hosting), the domain owner and root administrator, the service provider who maintains the service and business logic, and the consumer who owns the data at the endpoint.

Example: an end consumer who buys a sensor gets ownership of that sensor on the data layer. In the application layer, service providers can link services. They can access that consumer's sensor data. The consumer can remove the robot or sensor from the service, and the service provider then loses access.

The note says the Real Time Web is a plug-and-play heterogeneous network for machines. It says AI students understood the concept in about five minutes and then built services. Link given: https://nornir.io/ntnu-hackathon-brain-and-nornir/

This note does not name an independent GDPR audit or a certification. Do not invent one.

## Language and development-time claims

Unverified. The deck said the technology is language independent and offers "95% reduced development time." This answer says the model removes the server and middleware cycle (deployment, API, database, test, production). Synx tools are described as no-code or less-code infrastructure. Sending and receiving is said to work from any programming language, with no libraries installed in advance. Nornir is said to provide native source-code examples. This corpus does not include those examples.

Services and links can be done at runtime by commands to domain names. The note says an AI, robot, or application can create, integrate, and share data, and that an application can be built on demand and terminated after use. The example is an AI creating a chat program that leaves no trace after the session. Do not turn that into a how-to that is not written here.
