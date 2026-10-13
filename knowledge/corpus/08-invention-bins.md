# Bijective Network System (BiNS)

Invention notes titled "Real-Time Web Framework for Internet of Everything Systems. A bijective network system with distributed runtime BIOS." This is the invention write-up, not a public 2026 specification. Do not turn the command list into a live API. The public site still does not publish encodings or command tables. Quote a command only when they ask how, and say it comes from these notes.

## Four layers

Compared with OSI and TCP/IP, BiNS is backward compatible with TCP/IP and uses four layers:

1. Network and Restore. Persistence of anti-objects for restore and reboot. Allocation, logging, redundancy.
2. System. Health, error correction, security updates, logical addressing, system events.
3. Application. Command options for the Synx BIOS runtime. Sessions or linking between domains and services. Translation, encryption, compression.
4. Data. Endpoint and edge services. HTTPS, websocket, and other protocols. Ownership shipment and data-access commands.

The ghost module is shared memory so the active layers can communicate up and down.

Ghost types: data layer C-objects, application layer T-objects, system layer P-objects, network layer A-objects. Processing units in each layer update them. They also carry messages between layers.

Ownership: domain owners configure memory and CPU at the lower stack. System owners configure authentication. Service providers own semantics and transformation in the application layer. Consumers control data in the data layer. Lower layers can reach higher layers. Higher layers cannot reach lower layers.

## Keywords

Root domain is the DNS root, such as mydomain.com. A subdomain is subdomain.mydomain.com.

Service URI keeps the same path across protocols. HTTPS example: https://subdomain.mydomain.com/servicea Websocket: wss://subdomain.mydomain.com/servicea Another protocol would change only the scheme.

Primary service: the endpoints belong to it and the data schema is fixed. A sensor shipped from the factory connects to its primary service and cannot change that after shipment.

Secondary service: morphs an endpoint whose primary service is elsewhere. Arriving data uses the secondary schema after morphing.

Link: from one data element on the primary service to one data element on a secondary service. No limit is stated in this invention note.

Morphing: the endpoint is assimilated by the secondary service and adapts to that service's structure and intelligence.

Triplet: subject holds description, command schema, and data schema. Predicate and predicate noun hold internal logic or an external software agent. Object is a reference to a ghost, an endpoint, or a secondary service.

Predicate runs on linked data and fits it to the local schema before distribution to local endpoints and to services with an active link. Predicate noun runs after local endpoints have the data, and before a service with an active link receives it.

Channel: one connection can merge several services. Each may have its own schema. Access rules still apply.

Gateway: an endpoint whose real device is beyond TCP. Wi-Fi and ordinary routing are not gateways in this definition, because they have an IP address. LoRa, Dash7, Zigbee, and similar wireless sensors, where a gateway carries a proprietary payload, are gateways. They can be virtualized as passive bijective networks.

Passive object: no connectivity of its own. A can, a window, a meteorite. It can still be identified in context so a service generates data. Active object: connected, or a short HTTP client that closes after POST or GET. Its ghost still represents it.

Private network: one entity controls the domains. A service can be public, private, or protected. Public can be linked from another root domain. Private: others may create a link but it stays inactive, so no data flows. Protected: no active links, and hidden from search.

Data in this note is real-time data the network has not persisted before redistribution. Information is historical data.

Synx C-DNS: client domain name system, part of Synx BIOS, installed per root domain. Maps IP addresses to clients, services, subdomains, and root domains.

Synx Cat: the command matrix. Each command has a category number. Each layer can use only some categories.

## How a connection works

Some Synx category is added in the header to change the default TCP behaviour. Each service can allocate many ghosts. If authentication matches the ghost id, the endpoint is primary to that service. Otherwise it is secondary, and the primary service updates the secondary service when a linking path exists.

Data is distributed only when the same owner is at both ends. Along a complex path the data may be transformed many times. It still arrives if the owner is the same.

Inside one primary service, this note says endpoints can share with each other by default. The service owner can change that with a Synx Cat command so endpoints do not see each other's data.

The service owner owns the application logic. The consumer owns the network resource. The person who creates a link controls that relationship. Integration uses links. Any programming language. No extra library. HTTPS and websocket work. The ghost is one-to-one with the client instance and the ghost id.

The data schema is the key-value protocol, described on the micropage. The command schema is the service provider's commands and parameters.

The network communicates contextual data and supports the ASCII table. The source writes "ACII". Meaning is up to the service provider.

You may reshare data you collected, because it belongs to you. You may change data by setting up a service and linking. A consumer at the endpoint is also allowed to change their own data. Morphing fits their data to the provider's model. The logic of the morph belongs to the service provider.

You can tag a ghost id with a price. The note says there will be services that monetize who consumes the data. It does not name a live price list.

Links can be added or removed at runtime. Connected endpoints stay connected and see the change in the same session. The arrangement lasts while the link is active.

Transfer: give the ghost id to another person and they get the channel. Read access is a Synx BIOS command. Do not invent parameters that this note does not list.

## Synx Cat commands

The invention note's most-used list. Level is the layer where the command runs. The note says the set varies by version.

| Synx CAT | Description | Level |
|---|---|---|
| 0 | Send cmd. Incoming command messages to the service owner. | 4 |
| 1 | Send data. Incoming string from an endpoint. | 4 |
| 2 | Set public ghost. Make the endpoint ghost public and morphable. | 3 |
| 3 | Set mapID. Object id uses the id in mapID. | 2 |
| 4 | Data channel. Establish a data channel for the endpoint. | 4 |
| 5 | Dynamic channel. Channel merge. | 4 |
| 6 | Create service. | 3 |
| 7 | Allocate and add a ghost on a service URI. | 3 |
| 8 | Create a link between two services, by the primary service. | 3 |
| 9 | Create user. | 2 |
| 10 | Update service with new semantics. | 3 |
| 11 | Remove ghost. | 3 |
| 13 | List active connections on Synx Cat 4 and 5 for this owner. | 4 |
| 16 | Change owner on a ghost. | 2 |
| 18 | List ghosts in limbo, between owners. | 2 |
| 19 | Set owner. | 2 |
| 20 | Get resources for a user: ghosts, services, domains. | 3 and 2 |
| 21 | Ownership rejected. | 2 |
| 22 | Get domain. | 3 |
| 23 | Set token. Sets a new token on the user. | 2 |
| 24 | Kill the endpoint connection. | 2 and 4 |
| 25 | Add a morphed ghost to a secondary service. | 3 and 4 |
| 26 | Remove a morphed ghost. | 3 and 4 |
| 27 | Give read access to a user. | 2 and 4 |
| 28 | Remove read access. | 2 and 4 |
| 29 | Delete user. | 1, 2, 3, and 4 |
| 30 | Get subdomains. | 3 |
| 31 | Add or remove domains for a user. | 2 and 3 |
| 32 | Ghost resources. Status of a specific ghost. | 2 and 4 |
| 33 | Set domain. Activate the domain. | 3 |
| 34 | Change owner on a subdomain. | 2 |
| 51 | Activate log for a service on Synx Cat 0. | 2, 3, and 4 |

Parameters are mentioned but not tabulated. Do not invent them.

## Data flow rules

If there is no link in the application layer, no data is transferred between different services. Clients of the same primary service share updates by default, unless the owner changes that.

A service owner can kill one active connection. The endpoint gets a broken connection and can reconnect and authenticate again. The note also says an endpoint can be disabled permanently. It does not give a separate command number for the permanent case beyond the kill command in the table.

Software agent: if the connection authenticates as the service owner, the ghost is a T-ghost and gets application-layer commands. Command messages travel opposite to the data schema, and only across a direct link. Service A can command Service D if A links to D. A cannot command Service C if there is no direct link, even if C is further along the chain.

Robot and gateway picture: the gateway provider publishes a payload schema. The robot provider links to the gateway. The application links to the robot. Data flows only when the same user owns the robot ghost and the application ghost. Thousands of arms and millions of app instances can exist. Flow starts when ownership of a specific arm is transferred to a user who is also in the application. The gateway provider does not learn the user. The gateway can log a copy in its own schema. The application layer gets a copy in its own context.

Several routes: the default is the smallest route. A Synx command can accept all routes, which yields multiple messages. The note says that configuration is used when the network is a neural net. On a private intranet owned by one entity, predicates can be moved to the endpoint ghost and run sequentially in that memory, instead of sending the data around the network.

Anti-objects: clones of the ghosts in a graph database, holding triplets, ownership, and links, so a power loss can be restored. Semantic description for humans and search may live there too. Serialization of in-memory ghosts is optional and is for sharing across IP addresses.

Authentication: an external AIM system can be mapped at the system layer. The endpoint authenticates outside, receives an access token, and applies that token when sending to an RTW service. The token can be updated dynamically. Default in the note is a two-factor token from username and password, replaceable by an external IAM.

Multiple services in one channel: commands during an active connection can merge ghosts. The connection point stays. The data structure can change without a new session.

## Claims in the note

Peer-to-peer communication using bijective proxies in multiple layers, to separate access along the vertical value chain.

A runtime BIOS in the network stack, so middleware and server-side session and authentication systems are not required.

The network is independent of communication protocol. Endpoints do not install libraries or preprogrammed code to join.

Ownership and rights per layer. Users control data independently of the services that use the source.

## Consumer morphing example

A temperature sensor ships in Celsius to its primary service. The buyer adds it to a secondary service that turns a light on at 20 degrees. The secondary service morphs the device into itself. Data follows the linking path into the secondary schema. The channel runs until the consumer leaves, or until the service provider stops that endpoint's access. Each controls a different layer.
