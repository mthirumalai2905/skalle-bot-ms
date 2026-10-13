# Nornir.io Tech Corner

Older tech-corner and tutorial notes. The live trial named here is Cioty, at domain.cioty.com, with SynxPass at synxpass.com. These are not Morph Space screens. Do not invent a screen that is not described. Sample tokens in the source are replaced with a placeholder. Tell the person to use their own token.

## The Real Time Web

A collective machine network. Compared with Solid (Inrupt), led by Sir Tim Berners-Lee, which shares information with individual control, and the QUIC working group on HTTP/3 and UDP. Nornir's starting point was machines, not the human web. Real Time Web is a heterogeneous collective for autonomous machines, written in a language humans can understand.

## HIVE Collective

HIVE Mind is the metaphor, including the Star Trek Borg: each individual is stronger because it links to the collective. Synx HIVE is the tool collection. How intelligent a client can be is limited by its physical abilities.

Temperature-sensor example: the sensor only sends Celsius. Hundreds of applications can use that reading. Add the sensor to a secondary light-control service with a command and it inherits that service. The switch provider can turn lights on at 20 degrees and off at 15. The same sensor can be aimed at a coffee machine, a lock, or heat. The limit is the one data element. More services make the collective more intelligent. Behavior changes with the morphic service the device is running.

## Data versus information

The note rejects the Wikipedia line that data are characteristics or information collected through observation. In this definition, information is structured historical data. Data is the value before it is stored. Once it is in a database or filesystem it has become information. Machines distribute fresh data. Humans need information because they cannot process data fast enough.

The same data can trigger different processes. Context can change along the value chain. Billions of packages, millions of use cases. Links address the transformation. A link is a sentence: subject, predicate, object, following the Semantic Web. The predicate is the verb. You create a service name (subject) with a data model, link to another provider's data element (object), and add a predicate if you need to transform it, as an inline script or a software agent. The goal is to fit your local structure so the next link does not inherit inconsistent data.

Bidirectional linking uses the same path in the opposite direction, and this note limits that direction to commands from the owner of the primary service to a secondary service that offers commands.

## Morphic microservices

Morphic comes from morphogenesis and organising fields. A system inherits behaviour by tuning to a data channel, like a radio. Traditional microservices are one layer: you must know the structure and implement an API. A morphic service has no API implementation. The structure may change at runtime during an active connection. Bidirectional linking is supported by Synx BIOS, which segregates layers and access. No code libraries on the network resource. Stateful and stateless HTTP, HTTPS, and websocket over TCP.

The founders named for MAD: Paal Kristian Levang and Henrik Silverkant.

## Network ghosts

Backward compatible with TCP. Lower ISO layers are enhanced by Synx BIOS, which can move data up and down and segregate access. A client connects to its ghost, not to a platform session. The ghost is created at connection and disappears on disconnection. It exists when authenticated data is about to move, and the structure is inherited at runtime. The connection can be stateless, stateful, or both. Protocol independent. The service provider can change behavior and structure during the connection.

Ghost versus digital twin: a ghost can be used to make a digital-twin service, and also reaches lower stack layers. Hosting providers, security providers, and application providers are "passive" players in the note. To disconnect a pair using his service, the service provider sends a Synx command to kill the connection. Synx BIOS can move ownership, handle read access, and move ghosts between services at runtime. The ghost follows the user's signature.

## Background dates

Introduced in 2008 by Paal Kristian Levang and Henrik Silverkant, described here as a Swedish computer-security specialist. In 2008 they started Synaptic Technologies, which later became Nornir Holding. First Synx BIOS prototype in 2013. In 2014 Nornir was funded to take it to market. The note says there was no written MAD documentation until this tech corner, and invites others to explain it better.

## Why machines do not use the Web

Machines process data. They idle until input arrives. Platforms that make them talk use APIs, and the note calls large-scale interface implementation a dead end that produces silos. RTW is meant to link machine data with web sharing standards, without a preprogrammed task. No middleware or extra database to set up a service.

## Linked data for machines

Cross-linking private HIVE networks is what this note names the Real Time Web. Synx Tools had not fully implemented RDF/OWL in the HIVE version at domain.cioty.com. Regular expressions and basic metadata were used. Understanding Semantic Web still helps.

## User access and anonymity

SynxPass provides identity, single sign-in, and command options based on role. A domain owner gets more commands than a consumer. Ownership of a sensor can be transferred. From the moment the other person accepts, the previous owner cannot control it. Synx BIOS has a map ID so a blockchain or another method can be used for integrity. The note says to see a tutorial for the commands. It does not paste a full command list in this section.

Anonymous users: the network does not persist data, and domain owners do not control consumer data. The ethical dilemma they name is a robot that causes harm while the controller is unknown. They added SynxPass so every resource authenticates before a morphic service. The token stands in for username and password. Only if something bad happens can the user be backtraced from the SynxPass network log. SynxPass is not tightly integrated with Synx BIOS and can be replaced. Tokens are dynamic. Registration is required from root domain owners to consumers.

Two users on the same service URL can get different values with the same structure, for example a different language. Service providers see stack level 2 (application). Their predicates stay unexposed to each other.

## Stack matrix

The note's table. Ghost roles are letters. Treat the last row as their label, not as instructions.

| Stack level | Stack layer | Ghost | Access level | Connectivity |
|---|---|---|---|---|
| 1 | Data | C | Basic Synx commands only: register user, give ownership, accept ownership | HTTP, HTTPS, and socket. Client and server. Stateful and stateless |
| 2 | Application | T | Extended commands: register subdomain or service, set up a data link | Through a domain registrar such as cioty.com, a Synx HIVE controlled by Nornir |
| 3 | Domain | P | Root domain owner and super user on a private HIVE | Root maps the IP and basic HIVE configuration. Command line only |
| 4 | Physical | A | Root access and root domain registrar for private and public HIVE | Installation and environment control. Source repository |
| 5 | Protected | A | SynxPass command. The note's own words: backdoor root ghost access (anti objects). Can only be accessed by Agent Smith | Their label only |

The note says four levels of data distribution, five if you count the Pass layer. Each layer acts on the ghost independently.

## Practical IoT tip

Wireless protocols named: LoRaWAN, Dash7, Zigbee, NB-IoT, Wi-Fi, Bluetooth, Disruptive Technologies, Sigfox, TineMesh, and others. The gateway relays the carrier into TCP/IP. Hive is part of the TCP stack, so nothing is installed in the wireless protocol. Use the token and the objectID or mapID to identify the device when it enters TCP.

Virtualize the physical world. A public temperature service and a public movement service, with the gateway service kept private. Customers link to the sensor service. If several gateway technologies feed one sensor service, link them behind a common structure so the customer's path does not break.

## Machine learning and agents

The Cioty implementation was not configured for AI development. The note says to purchase a custom Synx HIVE from Nornir for that, and that a prototype is still possible on Cioty. The domain.cioty.com interface uses subject-predicate-object and is cumbersome for hundreds of nodes. Use command-line scripts. More information was at synxhive.com. This corpus does not include that site.

A software agent is a local client with TCP. Any language. It handles incoming command data. The simplest form is a callback that posts back to the primary service or a linked secondary service. An inline predicate is JavaScript for small transforms. Command-schema data cannot be handled by the inline script. A software agent handles commands, and is preferred for database writes or heavier analysis.

## Two FAQ answers

Can I monetize IoT devices on shipment? Yes. Each device talks to its own ghost. The assigned morphic service stays the primary service. After you give ownership of the ghost to the consumer, the device still sends to the primary service.

Why add a ghost from a secondary service? Data moves only if the user controls the resource on both ends. Add the user's ghost from the other service into your primary service. If a linking path exists, data is accessed from your primary ghost. The consumer who owns both ends is who the flow follows.
