# Whitepaper: Real-Time Web and Autonomous Machine Networks (Synx)

Norwegian sections in the source notes were translated into English. Outline headings with no body were kept as structure. This is not the same document as the 2017 NR whitepaper PDF. Link named in the source: https://docs.wixstatic.com/ugd/40ea63_bc0549cb461a4c518f536f50b4f9bd15.pdf

## What the Real Time Web is

The Real Time Web is a self-scaling network without a centralized server. The source says the stack was invented by Paal Kristian Levang and Henrik Silverkant in 2008. The work name was Morphic Architecture Design, influenced by Sir Tim Berners-Lee (the source writes "Sir Time Berners Lee") and biologist Rupert Sheldrake (the source writes "Rubert Sheldrake").

It is described as more than a protocol: decentralized operating-system functionality, an embedded domain-name service, and stateful or stateless communication, which is why they call it protocol independent.

MAD sets up a bidirectional multi-agent network and shares intelligence across domains so any connecting client can be powered. Data is morphed to the local structure of each service.

Backward compatible with the World Wide Web. WWW links historical information, documents and files. RTW separates data from information and distributes state changes along the linking path, transformed into each local Morphic Service so clients of that service can consume it.

Distribution is determined by ownership. Data from the source is consumed by a client that has the same ownership at both ends of the path. Each client gets a personalized channel. The source says this reduces load compared with traditional API communication.

## What Synx solves

Synx is a series of tools for domain owners, developers, and consumers.

Synx DNS lets creators set up domain names and morphic services, add intelligence, set up data links, and change the data structure.

Synx BIOS, expanded here as Basic Input Output System, lets users control data sources and administrate services. A command line, based on ownership and access rights. Consumers can share and transfer ownership or see data sources that belong to them.

Synx Pass: access control, authentication, encryption, and other security.

To join, a root domain is installed on a computer with a public IP. From there the user sets up subdomains and Morphic Services with the Synx tools.

Once services exist and agents support the service statement, clients can connect, or the service can link to other domains. A client adapts to the service it opens. Multiple services can be added to a channel, or one primary channel can link others and toggle.

Typical use: autonomous machines, where the AI creates, links, and changes services and channels at runtime.

## Why it matters in this paper

Machines need identity (personalized data), personality (AI behind the morphic service), and a body (IoT and sensors). Machines can share expertise in a collective. The source says what makes MAD different is that the user controls the data sources that feed the models, so data can be a tradable commodity.

Vision line repeated: eternal widespread ownership of the Web.

## Statefulness

A connection is against a ghost. The ghost is an interface to the stack layers.

Data layer: distribute from the source URI to the recipient where the same user owns the data.

Application layer: the linking path, transformation, and distribution outside the local domain.

Security layer: dynamic token and secret code, correct owner, ownership changes, and pending ownership transfers.

Lower network layer: redundancy. Operational settings are snapshotted. On reboot the latest setting is restored so message distribution in each layer continues.

The ghost is the client proxy and keeps state. The source says several clients can use the same ghost id so the client can scale by adding more clients.

## Self-organizing network

Anyone can set up a Morphic service. Each provider develops their own agents. To use another service, establish a link and transform the target data into the local structure. That is the only join step this section requires.

The network is self-organizing at runtime because the ghost operates in different layers concurrently. A service owner can change the data structure during an ongoing communication. An untrusted provider causes linking services to lose that data. A new link to a competitor is preferred. The tools do not judge quality. The source calls this a market-driven trial and failure process.

It can be a private network, one organisation end to end, or open, many parties, driven by consumers.

## Machines configuring the network

Synx commands are structured so machines can configure morphic services, set up links, and run a simulation to verify the setup. An AI agent can develop an app at runtime without a web server, and users can interact with it with no backend process. The source says what is needed can be done by a Synx command, and the application can be written by AI at runtime or fetched from the internet.

Synx BIOS is called a kind of digital nervous system. An AI agent is often related to a morphic service. One service can have many agents, each working independently.

The security, trust, and data-provenance heading in this paper has no body text.

## Use cases named here

New internet for machines: any physical or virtual object can receive intelligence. Channels are compared to a radio channel, except the data has been morphed. Examples: smart fridge, coffee machine, temperature sensor, alarms, then an AI agent, then a personal app.

Open like the Web. Nobody owns the network. You join by setting up a domain.

A service can be described before the data exists, and wake when the data appears. Useful to test a product before production.

Business flip: give away a physical sensor, price the data in the channel, and get paid by the app supplier. Compared to a telecom phone for 1 NOK with a two-year subscription. The difference claimed: RTW is not owned by one actor. Suppliers price services and build value chains as links. Demo video named: https://youtu.be/zRyF2WWN1PE

Intelligence, the umbrella: sensors for temperature, humidity, motion, and GPS. Body limits use. Video: https://www.youtube.com/watch?v=ITY5MawEM7Q The demo connects to YR.no for weather from GPS, can count raindrops, can receive a dating-service message, and has LEDs.

Automation, the orange bowl: https://www.youtube.com/watch?v=O0INc6pvrUc A bowl counts oranges and shows the count. Eating one updates the bowl. A light sensor estimates the count. Not exact.

Apen Ask: a browser animation linked to four AI services and an authenticated user channel. Face recognition, sign-to-speech, play tied to a curriculum, and audio. Used with children in kindergarten. The source says the same pattern is used for automated drones and humanoids.

NTNU hackathon video: https://www.youtube.com/watch?v=kNWXCyiSVxM The paper repeats the strong claim: over 100 AI master's students, healthcare, logistics, IoT, and games, live on stage after 24 hours, and an earlier Microsoft IoT hackathon that ended in slides. When repeating this, say it is this paper's account and point at the more careful field note on realtimeweb.org/blog/twenty-four-hours-at-ntnu

Intro video named: https://www.youtube.com/watch?v=CoqSlHJUoDA

Headings with no scenario text: smart-city energy and maintenance, industrial robots, humanoid elder care, urban mobility and droids. Later headings (architecture diagrams, deployment, business model, roadmap, conclusion) are an outline only.
