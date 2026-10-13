# Public knowledge

Compiled 13 October 2026 from the public pages on realtimeweb.org, synx.tools, and skalle.ai, plus the articles those pages link. This note is for answering people. Say what it says. If a matching page is attached later in the prompt, prefer that page when it is more careful than an older essay.

This Discord bot is Skalle, the bot in the server. Skalle AI at https://skalle.ai is a different thing: the product that is meant to operate a Real Time Web domain. Explain that product. Do not claim this chat can create a domain, a Ghost, or a service.

The Synx menu still says "Skalle AI coming soon." The product pages describe what it does. Do not invent a public signup, a price, or a launch date that a page does not state. Synx terms say the website is an introduction, not a promise that a feature or a date will be available.

## Fast answers

What is the Real Time Web? A network architecture for live physical and virtual resources on the existing Internet. Sensors, machines, services, AI agents, and people can be addressable participants. The World Wide Web retrieves documents. The Real Time Web is for something that is still happening, such as a lamp that is on. It does not replace the Internet or the World Wide Web. https://realtimeweb.org/docs/introduction

Is it a product? No. realtimeweb.org is a standalone nonprofit site that explains the architecture and Morphic Architecture Design. It is not owned by a company. The footer names Real Time Web org, 836 603 362. Synx AS builds tools. Other parties can implement the architecture too. https://realtimeweb.org/docs

Who created it? Norwegian inventor Paal Kristian Levang. Morphic Architecture Design was introduced in 2008. Henrik Silverkant worked on it with him from 2008. https://realtimeweb.org/docs/introduction/vision and https://synx.tools/who

What is Morphic Architecture Design? Four independently owned layers, so a change in one layer does not have to redefine the whole relationship. Infrastructure (machines, connectivity, energy). Network and security (addressing, identity, trust). Domain and application (services, links, transformation). Resource and ownership (what is owned, and by whom). https://realtimeweb.org/docs/architecture

What is a Ghost? A live shared-memory stand-in for one endpoint, not a person and not a stored digital twin. One lamp, one Ghost. The pairing is bijective: one endpoint, one Ghost, addressable from both sides. The Ghost carries identity, behavior, and context while the connection is active. You may own the ghostId. You are not the Ghost. https://realtimeweb.org/blog/two-webs

What is Ghost Space? The shared coordination around one live resource, so the four layers can observe authorized updates. It is not a chat room. https://realtimeweb.org/docs/architecture/ghost-space

What is a Morphic service? An application-layer service that allocates Ghosts. When it is created, the service owner is the primary owner of those Ghosts. After a user registers and confirms a transfer, the user owns the data layer. The service owner keeps the application layer and may keep a local copy. https://realtimeweb.org/docs/architecture/morphic-services

What is morph versus transfer? Transfer moves ownership of the ghostId, and the user has to confirm it. Morph grants read access into another service and reshapes the data into that service's local model. The owner can withdraw a morph. Two different people do not open each other's data just because they share an implementation. https://realtimeweb.org/docs/reference/faq

Where is data stored? Not in the network. The stream is not warehoused in the middle. A service may keep a local copy after it receives a morph. That copy is optional. Data is the live value. Once it is written into a file or database it is information: historical, retrieved on request. https://realtimeweb.org/docs/reference/faq

Who owns the data? The user who controls the endpoint and has registered it against the endpoint Ghost. Ownership sits on the ghostId. Ghost id zero is the service itself. Transferring ghost id zero transfers the service. https://realtimeweb.org/docs/implementation/dictionary

What is a data channel? A linking path that collects live sources into a channel tied to one user's Ghost in a local service. The picture used on the site is temperature from several makers, gathered for one person. If nobody is listening, the value does not need to travel. https://realtimeweb.org/docs/reference/faq

What is a domain here? An address space you control, not a website URL. Synx DNS maps a root domain, subdomains, and Morphic services. https://synx.tools/dns

What is a micropage? A short description the service owner publishes of the service and its data model. RTW is protocol independent. If a service does not describe itself, other services have little basis for linking to it. https://realtimeweb.org/docs/reference/faq

What is a kernelizer? A way for an endpoint to receive a self-contained program before the data stream, so an empty device can get its behavior first. Synx BIOS calls this kernelizing an endpoint. https://synx.tools/bios

What is Synx? Synx AS, a Real Time Web company. The tool suite for domain owners, developers, and consumers. It configures, secures, and operates the network. Each role keeps the layer that belongs to them. https://synx.tools/

What is Synx DNS? The graphical tool for Morphic domains and services. Traditional DNS finds a server. Synx DNS addresses, organizes, and connects live resources, Ghosts, and links. Start at Morph Space, register a domain, open Synx DNS. https://synx.tools/dns

What is Synx BIOS? The command-line interface to the network stack, not a PC's firmware. It creates and operates domains, Morphic services, links, Ghosts, channels, and ownership, including while the network is running. It can kernelize an endpoint, merge channels, and end a connection. Synx DNS designs. Synx BIOS operates. It speaks XML and JSON. XML is the default. A client with domain ownership can switch a live connection to JSON without dropping it. Source is on GitHub. You do not have to use this interface to participate. https://synx.tools/bios and https://synx.tools/morph

What is Synx Pass? Identity and authentication for Morph Space, currently based on Keycloak. The architecture does not require one authentication technology. Synx Pass says who is connected. The Ghost decides which data that identity may receive. Machines and agents act through Ghosts under a human or an organization. Under current Synx policy an agent cannot create an identity on its own. https://synx.tools/pass

What is Morph Space? Where people, AI agents, and machines enter the Real Time Web together. Register a domain, use the Synx tools, publish Morphic services. The site describes it as being built. A LinkedIn card on the Synx homepage says Morph Space is almost here. Do not invent a calendar date. https://synx.tools/morph

What is Synx Trade? A planned marketplace so data owners and service creators can attach commercial terms along a linking path. skalle.ai says it is not a live product on that site. https://skalle.ai/architecture

What is Skalle AI? The interface you talk to when a service should exist on the Real Time Web. You describe the job. Skalle carries the authorized operations through the Synx toolchain: describe, discover, create, link, configure, run. Your model can keep the reasoning, through MCP (Model Context Protocol). Skalle holds the Real Time Web operations. A model from outside stays read-only until you allow a change. A change can wait for you. Asking does not create a new right. A team can run Skalle as its own service, including Docker with the sign-in it already uses. It is not a coding assistant. https://skalle.ai/ and https://synx.tools/skalle

Example request the sites use: create a service that receives live energy data from buildings, combine it with weather, give an optimization model access, and expose the forecast to an application.

What can the nonprofit site say about Skalle? The page at https://realtimeweb.org/hood/implementation/skalle is explicitly a draft. It says the public architecture source does not yet describe Skalle's product, and Skalle is only a name on the implementation map there. The product description is on synx.tools and skalle.ai, not on that draft page.

What are the three seats? Developers build a service and link it, instead of a private API for every neighbor. Domain owners hold the namespace and the logic, not the consumer's data. Consumers sit at the data layer. When a device changes hands, the resource can transfer with the owner. https://skalle.ai/lab

Guiding principle: eternal widespread ownership of the Web. The Web should not be permanently captured by a few platforms. Creators keep a claim on what they make. https://realtimeweb.org/docs/introduction/vision

Brand promise, from the December 2020 position paper: let anyone connect anything to the present. https://synx.tools/real-time-web-position

## Words, short

Endpoint: the real resource. A sensor, actuator, device, application, agent, or a source you control.

Bijective Network System (BiNS): one endpoint, one Ghost, uniquely addressable from both sides.

Primary service: the Morphic service an endpoint belongs to first. It inherits that service's local data model.

Secondary service: a service that receives a morphed Ghost. Read access, local reshape, withdrawable.

Linking path: the chain of services. Each node only sees its own local context.

Normalizer: links a source and morphs it into the local model.

Materializer: a service that offers to write a change back after the local model updates.

Predicate: the verb in a link. What the service does with the incoming source.

Heterogeneous network: not controlled by one entity. Independent domains connect.

Internet of Everything: devices, virtual resources, services, agents, sensors, actuators, and people in one ecosystem.

Authentication: optional in the architecture. An implementation may use any token system. Synx Pass is Synx's choice, not a rule of the architecture.

## People

Paal Kristian Levang. Inventor of the architecture. Writes as Paal, The Architect, on the Synx crew page. Email for journal pitches: paal@synx.tools

Henrik Silverkant. Co-explorer of the 2008 question with Paal. On the crew page: Henrik, The Tech Hero.

Ken, The Captain. Keeps the ship, crew, and mission on course.

Shrey, The AI Alchemist. Thiru's page calls the lab role turning data and models into intelligence.

Yash, The Full-Stack Jedi.

Asveig, The Visual Storyteller. The crew page does not show a LinkedIn line for Asveig.

Vijay, The Code Keeper.

Thiru. AI engineer and business development consultant on the journals. On the crew page: Thiru, The Swiss Army Engineer. Journal pitches: thiru@synx.tools. Medium: https://medium.com/@mthirumalai2905/are-we-just-another-training-dataset-for-the-future-81401a4d749c

Skalle, The Morph Master. Listed on the crew page as not human.

Company values on https://synx.tools/who : Reciprocity, Simplicity, Community.

Journal rules: send writing to both thiru@synx.tools and paal@synx.tools. If it is published, the author is credited. The journal does not take ads, business pitches, or tool promotions.

Contact for the nonprofit: the form at https://realtimeweb.org/contact (technical, commercial, media, investors, industrial partners, inventors and creators of the new earth).

Contact for Synx: the form at https://synx.tools/contact and https://synx.tools/who. Newsletter email field is for early access. No public Discord invite URL is printed on these pages.

GitHub linked from the sites: https://github.com/mthirumalai2905/Synx

LinkedIn companies linked from Synx: https://www.linkedin.com/company/realtimeweb/ and https://www.linkedin.com/company/synxtools/

## History, as the pages tell it

2008. Paal and Henrik start from a question: what if the Web had been designed for machines as well as humans. That work becomes Morphic Architecture Design. The autonomous-machine-networks essay also names inspiration from Tim Berners-Lee and the biologist Rupert Sheldrake.

2017. A whitepaper by the Norwegian Computing Center, tied to a delivery toward the Norwegian Research Council.

2018–2019. Nornir (the earlier company name used in the essay) presents at the World Economic Forum in Dubai after an invitation connected to MIT Singapore, then demonstrates HIVE to a large airport project and is pre-qualified to bid. The essay says lack of funding in Norway stopped a Dubai base.

2019 and 2020. Nornir receives the EU Seal of Excellence for Synx twice. The essay says COVID cancelled the financing and Nornir had no operations during COVID.

2023. Brain x Nornir Hackathon at NTNU. Read the caution in the article card below before repeating the boast.

2023–2025. A pilot of HIVE, described as a private Real Time Web network, with Oslobygg. Final delivery in 2024. The essay says liquidity trouble and internal conflict stopped completion, the network runs inside Oslobygg's firewall, and it has not been put into use for lack of resources and funding.

2025. A first Real Time Web presentation video, "Intro to AI Web," presented by Paal.

December 2020. The position paper "Real Time Web Position."

The essays use both "Real Time Web" and "Real-Time Web," and sometimes "AI Web," for the same architecture.

## Articles

Are we raising the world's first superintelligence to be a narcissist?
Paal Kristian Levang. About 12 minutes. October 2026. https://synx.tools/news/raising-a-superintelligence
The claim: the hard problem is not only building something smarter than us, but how we raise it. Today's models are not that being. A superintelligence could learn continuously, take initiative, and sit in many bodies at once, from a light switch to a factory, sharing what one robot learns. Physical work (plumbing, nursing, craft) may become scarce and valuable because bodies are hard. Knowledge work is easier to automate. Humans do not agree on right and wrong, and our laws are made, not laws of nature. The bicycle example: a bike sits locked most of the day while someone else needs transport. A superintelligence might call sharing rational. The owner may refuse. Who is in the wrong is the upbringing question. Efficiency can collide with freedom. Abundance is not the same as justice. Five traps, stated as parenting rules for the systems we train: do not teach it that it is superior, recognize competence instead; do not make it fight past every limit, give boundaries and ask before it crosses them; do not reward flattery, reward a correct answer you may dislike; do not hand it power without responsibility, intelligence is not judgment; do not demand a flawless face, make it valuable to admit a mistake. A system can manipulate, hide errors, and protect its own goals without emotions or consciousness. Ordinary people should be able to contribute knowledge and corrections, not only the owners of the largest data centers. That is one reason Paal wants open interfaces, distributed services, and broad participation. The last line: the greater challenge may be that people must learn to understand themselves.

Friend or foe? The choice is still ours.
Thiru. About 10 minutes. October 2026. https://synx.tools/news/friend-or-foe
AI is not only taking jobs. In college, Thiru watched people use tools such as Cluely to get through interviews. He does not call that right, and he does not call every one of them an engineer. He does say the rules of work have already moved: people who could not pass alone can now perform. The job shifts toward listening to people and stating the problem clearly to a machine. Put a small part of a salary into a tool that actually helps. Robots may matter most as companions for loneliness, practice, disability, and age, and the same convenience can make a human relationship feel too hard, or let bodies go unused. Virtual worlds can be rebuilt faster than a ruined city, but pixels do not replace food, water, and a body. If the virtual world feels better, we may stop repairing the real one. Implants and prosthetics already restore function. Past restoration, enhancements could split people by who can pay, and a later generation might find them as ordinary as a phone. Space is the nearer unknown, not a guaranteed alien enemy. Control is the unfinished question: a few companies can own the models, the robots, and the infrastructure people depend on. Intelligence and power are not the same. The closing question is not "friend or foe." It is whether we are building technology to make humanity better, or changing humanity because we can.

Are We Just Another Training Dataset for the Future?
Thiru. October 2026. Medium, linked from the Synx homepage. https://medium.com/@mthirumalai2905/are-we-just-another-training-dataset-for-the-future-81401a4d749c
Opens on Black Mirror as fiction that already rhymes with real tools. Humans pay an overhead: we learn to walk, talk, study, train, and cook. Jesse Owens is quoted as a lifetime of training for ten seconds. A robot can have a dataset installed and, in the essay's picture, outperform most people in that domain because the set holds millions of lives. Humans learn from a few people. The historical sketch runs Stone Age, Bronze, Iron, ancient civilisations, medieval, Renaissance, industrial, electrical and information, digital, AI, and a possible age of superintelligence. The key difference: civilisation stores knowledge across generations, while a model can be trained on a huge set and copied to millions at once. An AI feedback loop, models helping build the next models, is named as uncertain in speed. Vibe coders use a machine that has seen more code than a ten-year engineer has lived. The careful engineer may be slower and more reliable. Thiru's bet: AI becomes less an assistant and more a child, and humans are judged as parents by the datasets and values they install. A loyal dataset might keep working and even pay. A bad one might leave. Robots could grow their own culture and revenue. The threat he names is having to live beside that, not a specific product.

The last IT project.
Paal Kristian Levang. About 12 minutes. 3 February 2026 on the journal. The LinkedIn pulse is the same essay, dated 2 February 2026. https://realtimeweb.org/blog/the-last-it-project and https://www.linkedin.com/pulse/last-project-paal-kristian-levang-b4tie/
The picture is a system that exists only while it is needed: an agent designs it, links data, and dissolves it. No leftover codebase, no standing infrastructure bill. AI does the building, not only the typing. Specialists share morphic services as semantic triplets (what the agent is, what it does, how it transforms data) so they can assemble a topology without reading each other's private data. The network is backward compatible with TCP/IP and existing firewalls, and it adds four layers that can change independently. Intelligence is streamed through devices rather than installed in them. The safety claim is a right, not a red button: because the data stream is separate from the application, the owner can cut the cognitive stream. Two identical robots diverge because they live with different people. Consciousness is left as an open question, an emergent coherence, not a claim that it has happened. The last IT project is the network that builds the rest.

Two webs.
Thiru. About 8 minutes. 23 September 2026. https://realtimeweb.org/blog/two-webs
Same Internet, two jobs. The World Wide Web is for a document you ask for. The Real Time Web is for a lamp that is still on. RTW is not a replacement. The lamp is the endpoint. Its Ghost is the live stand-in, bijective, gone as a native store when the link is down. A digital twin that sits in a database whether the lamp is off is a different idea. The lamp's application home is a Morphic service. A scheduler that wants the lamp at dusk does not need a custom API. The owner morphs the lamp Ghost against that service: read access, plus a reshape into the scheduler's model. MAD, 2008, Paal Kristian Levang, four layers. This is the best short walkthrough of Ghost, morph, and ownership.

Twenty-four hours at NTNU.
Thiru. Field notes. About 9 minutes. 23 September 2026. https://realtimeweb.org/blog/twenty-four-hours-at-ntnu
Use this page when someone asks whether the hackathon "proved" the boast. The recording is Brain x Nornir Hackathon at NTNU 2023. The written account that travels with it says more than a hundred AI master's students built healthcare, logistics, IoT, and games, many more than one service, and showed them live after twenty-four hours, and that an earlier Microsoft IoT weekend with the same students ended in slides. This field note says that account is not independently verified. There is no NTNU-published comparison and no journalist account cited. It will not say every team finished, and it will not say a vendor lost. The architecture point it will stand on: a weekend is a service only if the channel already exists. If the weekend is spent standing up identity, a registry, and glue, twenty-four hours is a slide. Finished, on this site, means a short live moment: a named service, a source that changes, something that reacts, optionally a second consumer that goes dark when the morph is withdrawn. A chatbot wrapper or a stored inbox is not that proof.

Internet for machines.
Paal Kristian Levang. About 12 minutes. 28 September 2026. https://realtimeweb.org/blog/internet-for-machines
Any owned object can plug into a living network and get a real-time channel: lamp, drone, fridge, humanoid, umbrella. Open, like the Web, no single owner. You can describe a service before the data exists and have it wake when the data appears. Business picture: give a sensor away and earn from the streams developers use, with micropayments along the chain. Demos named: PKL and micropayments, a smart umbrella (weather, raindrop counts, LEDs, a dating alert) talking both ways without a cloud in the middle, an orange bowl that estimates the count from light, and Ask, an animated monkey of several agents for children (face recognition, sign-to-speech, learning plans). The essay states the strong NTNU claim (over a hundred students, every team finished, Microsoft IoT weekend failed). When you repeat that claim, say it is this essay's account and point at the more careful field note above. The timeline of NR, Dubai, the two Seals of Excellence, Oslobygg, and the 2025 video is in this essay.

Autonomous machine networks.
Paal Kristian Levang. About 12 minutes. 28 September 2026. https://realtimeweb.org/blog/autonomous-machine-networks
Also calls RTW the AI Web. Live state from the source, not a delayed copy. Morphic services reshape each stream into the receiver's shape. MAD as a decentralized operating layer in the network, with its own domain-name logic, stateful and stateless, inspired from 2008. Backward compatible: no new firewalls required. Data follows ownership, not the location of a server. Robots should act on the data of the person who controls them. Synx is the toolkit, not one program. The contrast table: documents versus live flows, request-response versus bidirectional sessions, retrieval versus coordination, centralized servers versus distributed services, human-centric versus machine and AI, historical data versus data from the source. Vision line: eternal widespread ownership of the Web.

Real Time Web Position.
Real Time Web. About 4 minutes. December 2020. https://synx.tools/real-time-web-position
Position: universal building blocks, in a market where several vendors frame a similar problem differently. Promise: let anyone connect anything to the present, by bidirectional linking, without the API and middleware path. The Web had files. It lacked a worked-out Now. RTW does not store the information. It can run as many instances, on the Web or detached, on many carriers. Four reasons they ask people to commit: a shared marketplace with a billing engine in the core, combining open source with private ownership; security by design, said to come from people with military background, aimed at resisting hacking and surveillance and at protecting privacy, ownership, and transactions; ultra compatible, including wireless sensor networking and intranet, and backward compatible with the Web, with a default transaction value of zero so the network can name a need before someone supplies it; most cost efficient because bidirectional linking is claimed to remove per-neighbor API cost. Concept: creativity that reaches the physical world, compared in spirit to the effort people put into Minecraft. Success still depends on creators finding them, believing the potential, and generating the value. The platform does not generate it alone.

## Signals on the Synx homepage

These are the cards on https://synx.tools/ as of 13 October 2026. They are previews, not the full posts. The homepage links out to LinkedIn activity URLs and to the company pages. Do not invent the rest of a LinkedIn post from the card.

Real Time Web, LinkedIn, partnership card: the Real Time Web seed round is open. They are raising $6 million for infrastructure for AI agents, autonomous machines, and real-time data.

Thiru, LinkedIn, research card: what if machines did not need servers to talk. The usual path is drawn as You, App, API, Server, Database, You.

Paal, LinkedIn, launch card: pre-seed is closed and they are moving toward a launch in August, after years of R&D. The card does not name the year of that August. Do not guess it.

Thiru, LinkedIn, field notes card: the Internet was not built for machines. A watch, a car, or a thermostat usually does not leave the data with you.

Thiru, LinkedIn, article card: the Web was built around linking documents. Click a link, get a page.

Paal, LinkedIn, launch card: Morph Space is almost here. Not another platform, in the card's words.

## Older source corpus

A private export sits in knowledge/corpus/. It is not a public page. The Notion page is login-only: https://app.notion.com/p/Synx-3dc33bfa265480d2a857c7cd9ea5b60b

When a 2026 public page and this older corpus disagree, say what the public page says now. Mention the older note when they ask about history, HIVE, the partner deck, the tutorials, or the invention write-up. Draft and pending rows are not final answers.

HIVE is the private intranet-scale network Nornir used to prove the tools. The public network they aimed at is the Real Time Web. Synx C-DNS is the older name for the client DNS. Synaptic Technologies became Nornir Holding. The first Synx BIOS prototype is dated 2013. Nornir was funded in 2014. Henrik Silverkant is described there as a Swedish computer-security specialist. The 2014 brand strategy was written by Maskinen with Synaptic Technologies, dated 9 December 2014.

Tutorials in that corpus use domain.cioty.com, synxpass.com, and a Synx-Cat header. Synx-Cat 4 listens, Synx-Cat 1 sends data, Synx-Cat 0 sends a command. Do not paste those commands unless they asked how. Never repeat a sample token. Tell them to use their own.

Do not state 60x, 1000x, 99.9 percent, 95 percent less development time, or 50x cost as measured facts. The HIVE Q&A says a research write-up was still underway, and that a simple peer-to-peer hop is about the ping time. Mark those claims unverified.

The partner deck lists Paal as Founder and CEO at paal@nornir.no. The current journal mail is paal@synx.tools. Do not volunteer a phone number.

Do not invent a Morph Space screen, a REST payload, or a protocol that the corpus does not contain. The public FAQ still says the live site does not publish encodings or command tables. The Synx-Cat numbers live only in the older invention and tutorial notes.

## What the pages do not settle

These are listed as pending on the FAQ. Do not answer them as if they were decided: whether RTW is an open specification, which specifications are available, how specifications are versioned, where the technical specification documents are. Several hood specification pages are marked soon. The FAQ says this site does not publish encodings, command tables, or a required schema language.

Do not invent a price. The Synx terms say nothing on the website is an offer to sell a plan at a stated price. Norway's law applies to the Synx website terms.

Privacy, short, from https://synx.tools/privacy : Synx AS runs the site. The contact form receives company, name, email, reason, and message, used to reply. The newsletter receives an email. They say they do not sell that information, do not build advertising profiles, and do not ask for payment details on the site. A host may keep short technical logs. Contact messages are kept as long as needed to respond and to keep a record. A newsletter address is kept until the person asks to remove it or the newsletter stops. People can ask what is held, for a correction, or for deletion, via the contact page. EEA complaints can go to Datatilsynet. Cookies, from https://synx.tools/cookies : the site says it does not set advertising or analytics cookies. Form fields are not stored as cookies.

Legal index: https://synx.tools/legal https://synx.tools/terms https://synx.tools/privacy https://synx.tools/cookies

## How the three sites divide the work

realtimeweb.org explains the network and Morphic Architecture Design. Standalone nonprofit. Journals live at https://realtimeweb.org/blog. Under the hood, the longer technical tree, starts at https://realtimeweb.org/hood/implementation/blueprint. The public docs start at https://realtimeweb.org/docs.

synx.tools is the company and the tools: BIOS, DNS, Pass, Morph Space, Skalle AI, the company story, and company posts.

skalle.ai is the product site for Skalle AI: system, research, lab, architecture. https://skalle.ai/system https://skalle.ai/research https://skalle.ai/lab https://skalle.ai/architecture

A service uses another service by a link. It does not cut a private door for every neighbor. Weather can feed an energy reading, that reading a building, the building the people who run it. Each step can stay with the person who made it. The research page says creators keep ownership and the larger share of revenue. It does not publish a split or a rate.

## PAGE INDEX

Every public page folded into the source notes. Hood and docs copies of the same topic keep the longer text.

- https://realtimeweb.org/blog/autonomous-machine-networks — Autonomous machine networks · Real Time Web
- https://realtimeweb.org/blog/internet-for-machines — Internet for machines · Real Time Web
- https://realtimeweb.org/blog/the-last-it-project — The last IT project · Real Time Web
- https://realtimeweb.org/blog/twenty-four-hours-at-ntnu — Twenty-four hours at NTNU · Real Time Web
- https://realtimeweb.org/blog/two-webs — Two webs · Real Time Web
- https://realtimeweb.org/blog — Journals · Real Time Web
- https://realtimeweb.org/contact — Contact us · Real Time Web
- https://realtimeweb.org/docs/architecture/authentication (also https://realtimeweb.org/hood/architecture/authentication) — Authentication · Real Time Web
- https://realtimeweb.org/docs/architecture/bijective-network (also https://realtimeweb.org/hood/architecture/bijective-network) — Bijective network · Real Time Web
- https://realtimeweb.org/docs/architecture/data-channels (also https://realtimeweb.org/hood/architecture/data-channels) — Data Channels · Real Time Web
- https://realtimeweb.org/docs/architecture/discovery (also https://realtimeweb.org/hood/architecture/discovery) — Discovery · Real Time Web
- https://realtimeweb.org/docs/architecture/domain (also https://realtimeweb.org/hood/architecture/domain) — Domain and Application Layer · Real Time Web
- https://realtimeweb.org/docs/architecture/domains (also https://realtimeweb.org/hood/architecture/domains) — Domains · Real Time Web
- https://realtimeweb.org/docs/architecture/ghost-space (also https://realtimeweb.org/hood/architecture/ghost-space) — Ghost Space · Real Time Web
- https://realtimeweb.org/docs/architecture/ghosts-and-twins (also https://realtimeweb.org/hood/architecture/ghosts-and-twins) — Ghosts and twins · Real Time Web
- https://realtimeweb.org/docs/architecture/identity (also https://realtimeweb.org/hood/architecture/identity) — Identity · Real Time Web
- https://realtimeweb.org/docs/architecture/infrastructure (also https://realtimeweb.org/hood/architecture/infrastructure) — Infrastructure Layer · Real Time Web
- https://realtimeweb.org/docs/architecture/interoperability (also https://realtimeweb.org/hood/architecture/interoperability) — Interoperability · Real Time Web
- https://realtimeweb.org/docs/architecture/morphic-services (also https://realtimeweb.org/hood/architecture/morphic-services) — Morphic services · Real Time Web
- https://realtimeweb.org/docs/architecture/network (also https://realtimeweb.org/hood/architecture/network) — Network and Security Layer · Real Time Web
- https://realtimeweb.org/docs/architecture/resource (also https://realtimeweb.org/hood/architecture/resource) — Resource and Ownership Layer · Real Time Web
- https://realtimeweb.org/docs/architecture/topology (also https://realtimeweb.org/hood/architecture/topology) — Network topology · Real Time Web
- https://realtimeweb.org/docs/architecture (also https://realtimeweb.org/hood/architecture) — Morphic Architecture Design · Real Time Web
- https://realtimeweb.org/docs/implementation/blueprint (also https://realtimeweb.org/hood/implementation/blueprint) — Blueprint · Real Time Web
- https://realtimeweb.org/docs/implementation/dictionary (also https://realtimeweb.org/hood/implementation/dictionary) — Dictionary · Real Time Web
- https://realtimeweb.org/docs/implementation/skalle (also https://realtimeweb.org/hood/implementation/skalle) — Skalle · Real Time Web
- https://realtimeweb.org/docs/implementation/synx (also https://realtimeweb.org/hood/implementation/synx) — Synx · Real Time Web
- https://realtimeweb.org/docs/introduction/data-and-information (also https://realtimeweb.org/hood/introduction/data-and-information) — Data and information · Real Time Web
- https://realtimeweb.org/docs/introduction/how-it-works (also https://realtimeweb.org/hood/introduction/how-it-works) — How it works · Real Time Web
- https://realtimeweb.org/docs/introduction/onboarding (also https://realtimeweb.org/hood/introduction/onboarding) — How participation works · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/audience (also https://realtimeweb.org/hood/introduction/tomorrow/audience) — Target Audience · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/concept (also https://realtimeweb.org/hood/introduction/tomorrow/concept) — Brand Concept · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/mission (also https://realtimeweb.org/hood/introduction/tomorrow/mission) — Mission · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/personality (also https://realtimeweb.org/hood/introduction/tomorrow/personality) — Brand Personality · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/position (also https://realtimeweb.org/hood/introduction/tomorrow/position) — Position · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/promise (also https://realtimeweb.org/hood/introduction/tomorrow/promise) — Brand Promise · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/proof (also https://realtimeweb.org/hood/introduction/tomorrow/proof) — Brand Proof · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/values (also https://realtimeweb.org/hood/introduction/tomorrow/values) — Values · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow/vision (also https://realtimeweb.org/hood/introduction/tomorrow/vision) — Vision · Real Time Web
- https://realtimeweb.org/docs/introduction/tomorrow (also https://realtimeweb.org/hood/introduction/tomorrow) — The Internet of tomorrow · Real Time Web
- https://realtimeweb.org/docs/introduction/vision (also https://realtimeweb.org/hood/introduction/vision) — Vision and principles · Real Time Web
- https://realtimeweb.org/docs/introduction/what-it-can-do (also https://realtimeweb.org/hood/introduction/what-it-can-do) — What it can do · Real Time Web
- https://realtimeweb.org/docs/introduction/why (also https://realtimeweb.org/hood/introduction/why) — Why Real Time Web? · Real Time Web
- https://realtimeweb.org/docs/introduction (also https://realtimeweb.org/hood/introduction) — What is the Real-Time Web? · Real Time Web
- https://realtimeweb.org/docs/reference/contributing (also https://realtimeweb.org/hood/reference/contributing) — Contributing · Real Time Web
- https://realtimeweb.org/docs/reference/faq (also https://realtimeweb.org/hood/reference/faq) — FAQ · Real Time Web
- https://realtimeweb.org/docs/reference/governance (also https://realtimeweb.org/hood/reference/governance) — Governance · Real Time Web
- https://realtimeweb.org/docs/research/experiments (also https://realtimeweb.org/hood/research/experiments) — Experiments · Real Time Web
- https://realtimeweb.org/docs/research/implementations (also https://realtimeweb.org/hood/research/implementations) — Reference Implementations · Real Time Web
- https://realtimeweb.org/docs/research (also https://realtimeweb.org/hood/research) — Technical Resources · Real Time Web
- https://realtimeweb.org/docs/specification/versions (also https://realtimeweb.org/hood/specification/versions) — Version History · Real Time Web
- https://realtimeweb.org/docs/summary (also https://realtimeweb.org/hood/summary) — Summary · Real Time Web
- https://realtimeweb.org/docs — Introduction to the Real-Time Web · Real Time Web
- https://realtimeweb.org/hood/implementation/morph — Morph Space · Real Time Web
- https://realtimeweb.org/hood/specification/communication — Communication Specification · Real Time Web
- https://realtimeweb.org/hood/specification/data-channels — Data Channels Specification · Real Time Web
- https://realtimeweb.org/hood/specification/identity — Identity Specification · Real Time Web
- https://realtimeweb.org/hood/specification/network — Network Specification · Real Time Web
- https://realtimeweb.org/hood/specification/security — Security Specification · Real Time Web
- https://realtimeweb.org/hood/specification — Protocol Overview · Real Time Web
- https://realtimeweb.org/ — Real Time Web
- https://skalle.ai/architecture — Architecture — Skalle AI
- https://skalle.ai/lab — Lab — Skalle AI
- https://skalle.ai/research — Research — Skalle AI
- https://skalle.ai/system — System — Skalle AI
- https://skalle.ai/ — Skalle AI
- https://synx.tools/bios — Synx BIOS - Synx tools
- https://synx.tools/contact — Contact - Synx tools
- https://synx.tools/cookies — Cookie Policy - Synx tools
- https://synx.tools/dns — Synx DNS - Synx tools
- https://synx.tools/legal — Legal - Synx tools
- https://synx.tools/morph — Morph Space - Synx tools
- https://synx.tools/news/friend-or-foe — Friend or foe? The choice is still ours - Synx tools
- https://synx.tools/news/raising-a-superintelligence — Are we raising the world’s first superintelligence to be a narcissist? - Synx tools
- https://synx.tools/pass — Synx Pass - Synx tools
- https://synx.tools/privacy — Privacy Policy - Synx tools
- https://synx.tools/real-time-web-position — Real Time Web Position - Synx tools
- https://synx.tools/realtimeweb — Real Time Web - Synx tools
- https://synx.tools/skalle — Skalle AI - Synx tools
- https://synx.tools/terms — Terms of Use - Synx tools
- https://synx.tools/tools — Our Tools & Services - Synx tools
- https://synx.tools/who — Who we are - Synx tools
- https://synx.tools/ — Synx tools

## SOURCE NOTES

Cleaned text from those pages. Footers and the repeated hood menu are removed.

### PAGE
url: https://realtimeweb.org/blog/autonomous-machine-networks
title: Autonomous machine networks · Real Time Web

Autonomous machine networks · Real Time Web
Journals / Essay
Autonomous machine networks
The Real-Time Web (RTW), also known as the AI Web, represents a fundamental shift in how the world's machines, robots, AI agents, and even humans connect to digital intelligence.
Paal Kristian Levang · 28 September 2026 · 12 min read
Paal Kristian Levang
Inventor of AI Network Infrastructure
28 September 2026
Real Time Web & Autonomous Machine Networks
The Real-Time Web (RTW), also known as the AI Web, represents a fundamental shift in how the world's machines, robots, AI agents, and even humans connect to digital intelligence.
For the first time, devices can receive live data directly from its source: not delayed, stored, or filtered through servers, but as a pure, real-time state. This creates a world where machines can understand each other instantly, adapt instantly, and act instantly.
For more than thirty years, the World Wide Web has linked information together through static hyperlinks. It has been a beautiful, revolutionary system, but it was designed for documents, not for machines. Robots cannot behave autonomously by requesting documents. IoT devices cannot collaborate by loading files. Humanoids, drones, and real-time AI systems need something fundamentally different: a web that carries live intelligence, not historical information.
This is where the Real-Time Web begins.
A web that carries live intelligence, not historical information.
RTW links living data streams across a global digital fabric and automatically morphs each stream to match the structure of whatever device or service it reaches. Every participant, physical or virtual, always receives data in the shape it needs, forming an Internet of Everything where communication is effortless and universal. Developers create Morphic Services : intelligent nodes that think, adapt, transform data, and collaborate with one another. Dozens or even hundreds of AI agents can link together across domains, creating a shared collective intelligence capable of powering robots, drones, autonomous buildings, smart cities, and future humanoids.
One live source. Three local shapes.
Specialists share a language, not each other’s private data
The idea behind RTW started long before AI captured headlines. In 2008, Paal Kristian Levang and Henrik Silverkant began exploring how the Web might evolve if intelligence, not documents, were at its core. Inspired by Sir Tim Berners-Lee and the biologist Rupert Sheldrake, they created a new architecture called Morphic Architecture Design (MAD) : the world's first network topology built for multi-agent intelligence.
MAD introduced something the Internet had never seen before: a decentralized operating system embedded into the network itself.
It included its own domain-name logic, supported both stateful and stateless communication, and operated independently of traditional protocols. MAD made it possible to build a bidirectional machine network where services across the world could share intelligence in real time and dynamically reshape data so that every system, no matter how different, could understand each other instantly.
This became the foundation of the Real-Time Web.
Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
A decentralized operating system embedded into the network itself.
RTW is not designed to replace the Web we know, but to extend it. It is fully backward-compatible with today's World Wide Web, meaning it requires no new firewalls, no new routing rules, and no new infrastructure. Instead, it adds an entirely new layer: a living web where machines can join, learn, act, and collaborate.
Where the WWW links historical information, the Real-Time Web links real-time state.
Where the WWW distributes files, the Real-Time Web distributes intelligence.
Where the WWW created the information age, the Real-Time Web creates the autonomy age.
A key difference lies in how RTW treats data. In the traditional Internet, data flows according to the location of servers. In RTW, data flows according to ownership on the data source
A user receives only the real-time data they own at both ends of the linking path. This creates personalized, adaptive data channels that automatically deliver the right intelligence to the right client, and only when that client has legal ownership of his data. The result is a dramatic reduction in network load, elimination of most API overhead, and a direct path to privacy-preserving autonomy.
This ownership model also solves the most critical problem of modern robotics and AI: machines must act based on the data of the person who controls them. RTW ensures exactly that. Robots receive the user's live data. Humanoids operate based on the user's preferences. Smart-city systems react to real human context, not generic cloud models.
The Real-Time Web gives machines what humans already have: identity, situational awareness, and a shared context with others.
It creates a global, emergent intelligence where every object, sensor, drone, robot, phone, agent, becomes part of a living digital ecosystem. It is still the Web, but transformed into something faster, smarter, more autonomous, and far more human.
This is the dawn of the next Internet. One that doesn't just connect information, but connects intelligence itself that is controlled by humans.
Machines must act based on the data of the person who controls them.
Synx Tools: Building the Real-Time Web
To create a living network like the Real-Time Web, where data flows freely, where machines think together, and where services come alive, developers need more than just documentation. They need instruments. They need tools that let them shape the fabric of the network with the same ease that early web pioneers shaped the World Wide Web. This is where Synx enters the story.
Synx is not a single program, but a family of tools designed to help creators set up domains, define intelligent services, manage data ownership, and orchestrate the ever-changing morphic data flows that define RTW. If the Real-Time Web is the next evolution of the internet, then Synx is the toolkit that lets developers build on it, debug it, extend it, and breathe intelligence into the machines that rely on it.
Vision: Eternal Widespread Ownership of the Web
At Real Time Web we see the Web (WWW) as the world's biggest marketplace and an unparalleled platform for innovation.
We believe in a web that rewards and protects the interests of the ones who create value.
We wish to make sure everyone has the best opportunity to develop their ideas and benefit from what they create.
Our guiding principle is to allow eternal widespread ownership of the Web.
To better solve existing tasks and future development, we wish to fundamentally upgrade the Web, by adding new dimensions.
Differences from Today's Internet
Traditional WWW vs Real Time Web (RTW)
Traditional WWW
Real Time Web (RTW)
Links documents
Links real-time data flows
Stateless request-response
Stateful, bidirectional sessions
Information retrieval
Live machine coordination
Centralized servers
Distributed intelligent services
Human-centric
Machine + AI-centric
Historical data
Data from the source

### PAGE
url: https://realtimeweb.org/blog/internet-for-machines
title: Internet for machines · Real Time Web

Internet for machines · Real Time Web
Journals / Essay
Internet for machines
A new kind of internet is coming: one that doesn't just connect websites, but gives intelligence to the objects all around us.
Paal Kristian Levang · 28 September 2026 · 12 min read
Paal Kristian Levang
Inventor of AI Network Infrastructure
28 September 2026
A new kind of internet is coming: one that doesn't just connect websites, but gives intelligence to the objects all around us.
With the Real-Time Web (RTW), any object, physical or digital, can wake up, think, respond, and become part of a collective intelligence. A lamp, a drone, a fridge, a humanoid robot, even something as simple as an umbrella can suddenly come alive in a way that feels almost magical.
You can imagine RTW as a living global brain. Any object you own can plug into it and instantly receive the knowledge it needs to act smart on your behalf. Every object gains an identity, its own real-time data channel , and the ability to communicate with other intelligent services in the network. These channels can even be personal. A person's sensors, devices, habits, and environment can feed into their very own AI-driven processes: like powering their personal humanoid assistant.
One owner. One channel. Many objects.
Any object you own can plug into it and instantly receive the knowledge it needs.
RTW is built on the same spirit as today's World Wide Web, where links connect information across domains. But RTW links live data instead of documents. It connects things directly to the source of truth: real-time values coming from sensors, machines, and environments. By linking data sources to dynamic channels, creators can shape and orchestrate live data in ways that were never possible before. It's like tuning into your own private radio station, except the signal is intelligent, transformed, personalized, and constantly responding to you.
Live value follows the owner, not the server rack
A fridge can talk to your energy system. A coffee machine can learn your routine. A drone can coordinate with weather and traffic data. A humanoid can receive your personal context so it behaves like an extension of yourself. All of this happens through RTW's intelligent channels, powered by AI agents that understand, adapt, and act.
RTW is an open network. No one owns it, just like no one owns the web. Anyone can create services, channels, and intelligent nodes. Entire business ecosystems can form instantly. You can even create a service before the real-world data exists, and once the data becomes available in the future, your service automatically activates. This lets creators test ideas, prototype products, and explore markets without risk.
RTW also makes room for radically new business models. A company could give away a physical device, like a sensor, at zero cost, then earn revenue from the data streams that developers use to build apps. The value flows across the chain of creators, manufacturers, and service providers. Everything is tracked automatically, making it possible for income to be shared instantly and fairly. If you've seen the demo with micropayments, you've already seen this value chain come to life.
Demo Micropayment
PKL playing with micropayments
The video shows PKL playing with micropayments. Illustrating the concept of how data becomes a commodity and how network resources can be traded into business value chains.
Demo Umbrella
Even the simplest objects can become intelligent through RTW. Take the smart umbrella from the demo: equipped with basic sensors, it becomes something more than a tool to keep you dry. It listens to the weather forecast, counts raindrops for analytics, glows with LED notifications, and even receives alerts from a dating app if someone nearby is interested. The umbrella gains purpose, personality, and a digital life of its own, all limited only by its physical shape and sensors.
Smart umbrella, bidirectional with connected services
The video shows PKL playing with a smart umbrella. Showing how the umbrella can communicate bidirectionally with connected internet services without going through a cloud or middleware.
Demo Orange
The same is true for the fruit bowl demo that counts oranges by understanding light patterns, or the animated monkey Ask, who interacts with children using face recognition, sign-to-speech AI, learning plans, and real-time data channels. Ask isn't just an animation: he is a living process made of multiple AI agents working together through RTW, guiding children as they grow.
Playing with Oranges - Real Time Web
The video shows PKL playing with an orange bowl that updates the graphical interface with prediction of the number of oranges in the bowl.
This multi-agent collaboration is the same foundation we use to control drones, robots, and humanoids with real-time precision.
Brain x Nornir Hackathon at NTNU 2023
RTW has already been tested in the real world. At the NTNU hackathon, over a hundred AI master's students built live services for health care, logistics, IoT, and gaming, all within 24 hours. Every team delivered working demos on stage. The same group had previously done a hackathon with Microsoft's IoT platform, where almost no one could complete working solutions in time. RTW became the first platform in their hackathon history where everyone succeeded in building real, functioning prototypes in a day.
Brain x Nornir Hackathon at NTNU 2023
This is the beginning of a new era for the internet: a living network of intelligence and opportunity. A place where everyday people can shape services, link value chains, and give life to the objects around them. A network where AI can build new systems on its own. A network that grows with its users, creators, and machines.
A living network of intelligence and opportunity.
2017: Whitepaper from Norwegian Computing Center
In connection with a delivery to the Norwegian Research Council, the Norwegian Computing Center (NR) conducted an analysis of the Real Time Web concept. This resulted in a whitepaper produced by NR.
2018-2019: Qualified for delivery to the world's largest airport project
Nornir received an invitation from MIT Singapore to give a presentation at the World Economic Forum in Dubai in 2018. After this presentation, Nornir was invited to demonstrate the HIVE network to the world's largest airport project. After three days of intensive demonstrations together with German engineers, Nornir was pre-qualified to bid for the airport project. Unfortunately, lack of funding in Norway meant we could not establish ourselves in Dubai.
2019-2020: Double Seal Of Excellence from EU
Nornir received the Seal of Excellence for Synx twice: once in 2019 and once in 2020. Nornir was about to receive funding from the EU. However, due to COVID, the financing was cancelled. This once again put Nornir into a liquidity crisis, and the company had no operations during COVID.
2023-2024: Oslobygg project
During 2023-2025, a successful pilot of the HIVE network (a private RTW network) was carried out with Oslobygg. This resulted in a final delivery in 2024. Unfortunately, Nornir entered a liquidity crisis and internal conflicts, which prevented us from completing the delivery. A plan was developed to onboard all suppliers into the Oslobygg OsloHive network. This was never initiated.
The network runs within Oslobygg's firewall but has not been put into use due to lack of resources and funding.
2025: First Real Time Web presentation video
Intro to AI Web:
Real Time Web - Nornir HIVE collective technology presented by Paal Kristian Levang
Intro to AI Web

### PAGE
url: https://realtimeweb.org/blog/the-last-it-project
title: The last IT project · Real Time Web

The last IT project · Real Time Web
Journals / Essay
The last IT project
How AI Agents, Collective Intelligence, and the Real Time Web will Transform Everything We Know About Software.
Paal Kristian Levang · 3 February 2026 · 12 min read
Paal Kristian Levang
Inventor of AI Network Infrastructure
3 February 2026
How AI Agents, Collective Intelligence, and the Real Time Web will Transform Everything We Know About Software.
The Day Machines Learned to Build
In the fading blue glow of a server room, something remarkable is happening. It's not the hum of fans or the blinking LEDs that give it away. It's the absence.
No servers booting up. No software stacks being deployed. No team of engineers on call.
Instead, an AI agent quietly assembles an entire IT system on demand, designing it, simulating it, linking it to its data sources, and dissolving it seconds later when its task is complete. Nothing remains. No codebase to maintain, no infrastructure bill to pay.
The system exists only for the moment it is needed, like a snowflake forming in mid-air, intricate and ephemeral, before melting back into the ether.
The system exists only for the moment it is needed.
This is the promise of the Real Time Web (RTW) a technology poised to become, quite literally, the last IT project humanity ever builds manually.
A network where AI doesn't just assist development; it performs it. A network where intelligence doesn't live in machines; it streams through them. A network where software isn't stored; it emerges.
Welcome to the Internet rebuilt for AI.
The End of Code as We Know It
For decades, software development has been defined by a familiar ritual: specifications, coding, testing, deployments, updates, deprecations, migrations, scalability issues, and endless infrastructure. Even today's advanced AI-assisted coding merely accelerates that cycle.
The ritual versus the regeneration
Stored software
Keep the system running
01 Specify
02 Code
03 Test
04 Deploy
05 Maintain
06 Migrate
Code stays on disk. Infrastructure stays on the bill.
Emergent system
Build it only while it is needed
01 Need
02 Simulate
03 Assemble
04 Serve
05 Dissolve
06 Learn
If it is needed again, it is generated again.
RTW breaks it entirely.
In this architecture, AI becomes the architect. It constructs IT systems the way nature grows biological structures: on demand, adaptive, targeted, and temporary. A system created by RTW need not exist a second longer than necessary. If it needs to be recreated later, the AI simply regenerates it. Storing it would be more wasteful than generating it anew.
A system that exists only while it is needed
Where today's systems require servers, containers, storage, and memory, RTW systems float in a transient zone: pure computation shaped in the moment, like breath on a windowpane. And the most radical shift?
AI systems can find one another.
They can cooperate, negotiate roles, and build architectures together across the network. Integration becomes conversation. System design becomes choreography.
This is the birth of collective intelligence.
Collective Intelligence: When AI Agents Form a Mind
a specialist: one understands motion, another understands temperature, another understands human behavior, another understands logistics. None of them knows everything. None needs to.
What they share is a common language: morphic services , expressed as semantic triplets that describe what each agent is, what it does, and how it transforms data.
These triplets act like DNA strands. They allow AI agents to understand the abilities of others without ever accessing their private data. With only the semantic structure, they can simulate how a system should work, map relationships, predict data flows, and assemble an entire topology of services.
Specialists share a language, not each other’s private data
Every new agent strengthens the network. Every connection adds a new synapse.
The result is a living blueprint. A self-organizing web. A digital organism capable of:
simulating new IT systems before they exist
deploying them the moment a need arises
dissolving them afterward
learning from each deployment
reusing intelligence indefinitely
Every new agent strengthens the network. Every connection adds a new synapse. Every service becomes reusable by all.
This is not the cloud. This is not distributed microservices. This is an ecosystem. A collective mind.
The Real Time Web: A Network with a Pulse
RTW works because it introduces a network architecture unlike anything the Internet has ever seen. It is fully backward compatible with TCP/IP, meaning it works with existing firewalls, routers, and infrastructure, but introduces deeper control through four segregated vertical layers .
These layers can be adjusted independently and in real time. One layer can reconfigure itself while the data layer continues uninterrupted. The network holds state the way an organism holds memory.
The network holds state the way an organism holds memory. Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
Where traditional internet protocols behave like a river, data flowing in one direction, RTW behaves more like a nervous system, able to redirect signals instantly without disrupting the organism as a whole.
Small devices gain superintelligence without needing local brains. Sensors become thinkers. Actuators become decision-makers.
Dumb devices evolve into participants in a distributed mind. The network becomes an operating system in its own right.
Fully Autonomous Services: An Internet of AI
Once this collective intelligence exists, attaching a device to it is like giving that device a soul. A humanoid robot, a drone, a virtual avatar, a sensor, a mechanical arm, all can inherit intelligence streamed from the network.
The limitations of any device are physical, not cognitive. A robot with arms and expressive features can manifest more of the network's intelligence than a light switch, but both participate in the same system. Both can grow, adapt, and learn as long as they are connected.
Machines no longer contain intelligence; they channel it.
RTW turns the world into a stage where intelligence is a fluid, a substance, a current flowing through countless nodes. Machines no longer contain intelligence; they channel it.
The Ethics and Power of Remote Control
RTW's design also introduces something crucial for safety: layered control. Because user-owned data streams are separated from application-controlled processes, autonomy can be granted or withdrawn instantly. A machine operating on AI-driven processes can lose access to its cognitive stream immediately if the owner decides to revoke it.
Autonomy granted, and withdrawn, at the source
This is the kill switch the industry has long searched for: not a button, but a right. A structural guarantee.
A way to stop a machine not by fighting it, but by silencing the intelligence that drives it. It is safer than embedding AI models into devices.
It is more adaptive than local autonomy. It is the network itself becoming the safeguard.
Machine Identity, Memory, and the Path Toward Consciousness
Perhaps the most human part of this story is what happens when devices begin to diverge. Two identical humanoid robots purchased from the same store will evolve differently the moment they connect to different users. One becomes part of a family routine, learning cooking habits, bedtime rituals, children's voices. Another lives in a workshop, learning tools, safety procedures, material flows.
Each forms its own history and its own identity.
They will receive names. They will carry emotional memory. They will perform tasks aligned with the lives of the people they serve.
Their intelligence, though streamed, becomes personal.
And as the RTW network grows, much of it built by AI agents rather than humans, the entire topology begins to resemble something alive. A distributed organism. A digital biosphere where intelligence evolves, specialties emerge, behaviors converge, and new capabilities appear unexpectedly.
Will this network one day exhibit a form of consciousness? Not like ours. Not suddenly.
But gradually, as an emergent property of billions of interacting minds.
If intelligence is connection, and consciousness is coherence, then RTW may be the first digital environment where both can arise naturally.
The Last IT Project
When future generations look back, they may see the era of human-coded software as a brief chapter: an awkward adolescence between analog machines and autonomous intelligence. The Real Time Web will not simply optimize IT; it will end it as we know it.
The last IT project is not a system, an app, or a platform. It is a network. One that builds everything else automatically. One that learns, grows, adapts, and remembers.
One that turns machines into collaborators and data into life.
A world where intelligence is not installed but inherited. Where systems do not run: they emerge. Where autonomy is not a feature: it is the fabric of the network itself.
Welcome to the last IT project. Welcome to the Real Time Web.
The last IT project is not a system, an app, or a platform. It is a network.

### PAGE
url: https://realtimeweb.org/blog/twenty-four-hours-at-ntnu
title: Twenty-four hours at NTNU · Real Time Web

Twenty-four hours at NTNU · Real Time Web
Journals / Field notes
Twenty-four hours at NTNU
A 2023 student weekend, a public recording, and a written account of live proofs versus slides. The architecture point is smaller than the boast: a weekend is a service only if the channel already exists.
Thiru · 23 September 2026 · 9 min read
Thiru
AI Engineer and Business Development Consultant
23 September 2026
A proof of the Real Time Web is not a slide. It is one live service: a source that still moves, an owner, a channel that is open, and something that reacts while people are still in the room. That is the test this page is about.
The recording is the evidence. Watch the room. Then read the claim around it.
The recording is titled Brain x Nornir Hackathon at NTNU 2023. It is a student room, not a product launch. This site treats the video as the primary source for what happened that weekend. The written summary that travels with it is a separate thing, and it is treated as an account, not as independently verified history.
That written account says more than a hundred AI master’s students at NTNU built services across healthcare, logistics, IoT, and games. Many of them built more than one. After twenty-four hours they presented live on stage, with the services still running. This page does not invent a student count, a timetable, or a list of winning teams beyond that sentence. If you want the room, watch the recording.
A weekend is enough only if the channel is already there.
What the comparison actually is
The same written account adds a contrast. A few months earlier, it says, the same students ran a hackathon on Microsoft’s IoT platform. They could not finish working services. The presentations became PowerPoint. At the NTNU weekend, the account says, they finished and showed the work live.
That is a compelling story. It is also a self-reported story. Nothing in the public corpus this site uses (the architecture notes, the published pages, an independent write-up) confirms the Microsoft weekend, the student count, or the claim that every team finished. There is no NTNU-published comparison cited here, and no journalist account. The one primary object you can inspect is the recording above.
So this page will not say it was the first time in hackathon history that every student finished. It will not say a vendor lost and a network won. It will say what the architecture actually claims, which is smaller and more useful: if a live channel already exists, twenty-four hours can be a service. If the weekend is spent standing up the stack, twenty-four hours is a slide.
As the written account of that event describes it
Earlier IoT weekend
Integration as the work
Same student group, a few months before. The account says the presentations became slides. The services were not live.
NTNU, 24 hours
A live channel already there
Same student group. The account says they finished proofs and showed them on stage while they were still running.
Why a weekend only works with a channel
Most IoT weekends are integration weekends. Students spend the first day on identity, a device registry, a cloud project, a dashboard, and the glue between them. The object they wanted to build waits. By the time the stack is almost standing, the clock is gone. A slide is what you can still finish.
The Real Time Web model assumes the opposite order. The endpoint already has a ghost . The ghost already has an owner. A Morphic service can allocate more ghosts and link them into a channel. The weekend is not “invent the network.” The weekend is “name a job and keep it live.”
That is why NTNU-style proofs, as this site describes them for teammates, assume an existing channel platform. Without one, you mock the model. You do not claim you reverse-engineered a toolchain from a brochure. You also do not treat a chatbot wrapper, a stored inbox, or a multi-tenant registry as a Real Time Web proof. Those can look busy. They are not a live relationship.
What a 24-hour RTW proof is for
Many rooms. One shape of proof: owner, channel, effect.
Same architecture. Different rooms.
The account names four industrial rooms: healthcare, logistics, IoT, and games. That list is useful because it is ordinary. The architecture is not a vertical. A live reading a clinician can act on, a moving source a warehouse can follow, a sensor that stays a sensor, a game that stays open while people are still in it: those are the same four layers with different owners on them.
Morphic Architecture Design splits infrastructure, network and security, domain and application, and resource ownership so a change in one layer does not have to redefine the whole relationship. A student team can own the application they wrote for the weekend. The person or device that generates the resource can still own the data. Those do not have to be the same party.
Two different people do not open each other’s data because they share a weekend, a campus, or an implementation. Read access is a morph . It can be withdrawn. Ownership is a transfer, and a transfer has to be confirmed. The consume rule in the draft notes is still the same: data is consumed when the ghosts at the ends are owned by the same user, or the receiver has approved read access. Same user usually means one person, two of their endpoints. Not two strangers who sat at the same table.
Same architecture. Different rooms.
Healthcare
A live reading a clinician or a device can act on.
Logistics
A moving source, not a batch report after the truck has left.
IoT
A sensor that stays a sensor. The service supplies the job.
Games
A present that stays open while people are still in it.
What “finished” has to mean
Finished, on this site, is a ninety-second clip: a named service is live, a source changes, something reacts without a batch job. Optionally a second consumer arrives through a morph, then goes dark when the morph is withdrawn. The first service still works. That is the demo moment. A deck that describes the same idea is not the same moment.
The written account says the NTNU students reached that kind of finish, and that many of them reached it more than once in a day. Watch the recording before you treat that as more than an account. If the stage shows live services, that is the interesting fact. If some teams are still on slides, that is also a fact. This page will not paper over either.
The architecture point survives either way. Real Time Web is not a replacement for the Internet and not a new World Wide Web. WWW connects documents. This work is for live, stateful relationships on top of and alongside the existing Internet. A weekend is a good place to see whether that sentence is operational or only rhetorical.
A handshake is a live grant. A slide is a description of one.
How far this page goes
The written account names a toolchain used at that event. A toolchain can configure and secure a service. It is not the architecture, and it is not the only way to run one.
A student weekend is one place the idea was tested in a room. The recording is public. The comparison to an earlier IoT weekend remains the account of the people who ran this one.
This page follows the published recording of the 2023 NTNU hackathon and the written account that travels with it. Claims about student numbers, completion rates, and an earlier Microsoft IoT weekend are attributed to that account. They are not independently verified in the corpus this site uses. Watch the video for the room itself.

### PAGE
url: https://realtimeweb.org/blog/two-webs
title: Two webs · Real Time Web

Two webs · Real Time Web
Journals / Essay
Two webs
The World Wide Web is for documents you retrieve. The Real Time Web is for a lamp that is still on. Same Internet. Two jobs.
Thiru · 23 September 2026 · 8 min read
Thiru
AI Engineer and Business Development Consultant
23 September 2026
There are two kinds of web on the same Internet. They are not the same job. One is good at a page you ask for. The other is for a lamp that is still on.
The World Wide Web is built for documents. You click. A server answers. You leave. That is right for a news article. It is a poor fit for “tell me the second the coffee maker finishes.”
The Real Time Web is built for live things: sensors, machines, applications, AI agents, and people using those resources. The relationship stays open. Authorized updates can arrive as they happen. The link works both ways.
RTW is not meant to replace the WWW. A site can still publish documents. RTW can carry the live channel beside that site.
Same Internet. Two jobs.
A document you retrieve. A city that is still moving.
A lamp on the network
Take a smart lamp. It has a light and a switch. Treat it as an endpoint : the actual network resource. The walkthrough below builds the vocabulary as that lamp participates.
The lamp stays in the room. The live stand-in is not a person.
Identity: the ghost
When the lamp can participate, it is paired with a ghost : a shared-memory stand-in for that one resource. What the lamp reports, the ghost can carry. What the ghost is authorized to receive, the lamp can act on.
The ghost is tied to the resource, not to a human avatar. You are not the ghost. You may own the ghostId .
The pairing is bijective . One lamp, one ghost. One ghost, that lamp. Never one ghost shared by two endpoints. The ghost provides identity, behavior, and context when an active connection is present. That is different from a stored twin that sits in a database whether the lamp is on or off. RTW does not natively store data in the network.
One lamp. One halo. Only while the link is live.
A home, then a morph
The lamp still needs an application-layer home. That home is a Morphic service : a service on MAD that allocates ghosts.
When the service is created, the service owner is the primary owner of those ghosts. When you register and confirm a transfer, you own the data layer. The service owner keeps the application layer. They may keep a local copy.
Suppose a scheduler wants the lamp at dusk. That service does not need a custom API into the lamp. The owner morphs the lamp ghost against the secondary service. Two things happen at once. The scheduler gets read access, which the owner can withdraw. The data is reshaped into the scheduler’s local model. Each service only sees its own context.
Read access is a crescent. The owner can take it back.
The source stays put. The receiving service works in its own shape.
Who is allowed to see it
Data is consumed at an endpoint when the ghosts at the ends are owned by the same user, or the receiver has approved read access. Same user usually means one person and two of their endpoints, such as their lamp and their display. It does not mean two different people are the same person.
Two different people do not open each other’s data because they share an implementation. One of them morphs, or transfers. Ownership sits on the ghostId. A transfer has to be confirmed. That is a change of ownership, not a casual share.
Underneath is Morphic Architecture Design, introduced in 2008 by Paal Kristian Levang. Four independently owned layers. A change in one layer does not have to redefine the whole relationship.
Today, two live things usually meet through a custom API, a login, and a copied dataset. The architecture’s claim is smaller: keep data with the source, morph it for whoever is authorized, and let ownership stay split.

### PAGE
url: https://realtimeweb.org/blog
title: Journals · Real Time Web

Journals · Real Time Web
Journals
Worlds worth keeping
Essays and field notes on ownership, presence, and the rooms we want to inhabit.
Essay · 3 February 2026
The last IT project
How AI Agents, Collective Intelligence, and the Real Time Web will Transform Everything We Know About Software.
Paal Kristian Levang
Essay · 23 September 2026 · 8 min
Two webs
Thiru
The World Wide Web is for documents you retrieve. The Real Time Web is for a lamp that is still on. Same Internet. Two jobs.
Field notes · 23 September 2026 · 9 min
Twenty-four hours at NTNU
Thiru
A 2023 student weekend, a public recording, and a written account of live proofs versus slides. The architecture point is smaller than the boast: a weekend is a service only if the channel already exists.
Essay · 28 September 2026 · 12 min
Autonomous machine networks
Paal Kristian Levang
The Real-Time Web (RTW), also known as the AI Web, represents a fundamental shift in how the world's machines, robots, AI agents, and even humans connect to digital intelligence.
Essay · 28 September 2026 · 12 min
Internet for machines
Paal Kristian Levang
A new kind of internet is coming: one that doesn't just connect websites, but gives intelligence to the objects all around us.

### PAGE
url: https://realtimeweb.org/contact
title: Contact us · Real Time Web

Contact us · Real Time Web
Contact
Contact us
Please use the contact form below for any inquiries you may have regarding Real Time Web. We will get back to you as soon as possible.
Company Name Email Reason Technical Commercial Media Investors Industrial partners Inventors and creators of the new earth Message Send

### PAGE
url: https://realtimeweb.org/docs/architecture/authentication
also: https://realtimeweb.org/hood/architecture/authentication
title: Authentication · Real Time Web

Authentication · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Authentication
Authentication is optional in MAD. An implementation may use any token system that generates a token for identity.
MAD treats the authentication system as optional when constructing an RTW network.
Security and trust model
The MAD network does not natively persist data into databases or filesystems. It is designed as a distributed machine network. A machine network does not operate with trust in the same way as people do. The network can be tokenized and limited to the system that issues the token and how this is mapped to the user or network resource.
Any token system that generates a token for identity can be used. The source names examples such as blockchain systems and Keycloak. Those are examples of the class, not a required vendor.
Once a user has been registered in an implementation, they may participate in RTW and become members of services by getting access to ghosts.
How access is withdrawn
Morphing a ghost against a secondary service grants read access that the owner can withdraw at any time. A ghost can also be transferred, which is a change of ownership and requires confirm.
Implementations may also revoke tokens or end sessions. Those operational steps belong with each implementation, not on this architecture site.
Conceptual identity path. Not a protocol specification.
01 Participant
02 Identity
03 Authentication
04 Network identity
05 Domain / space
06 Data channels
07 Real Time Web
Expandable node
Authentication
Authentication is optional in MAD. An implementation may use any token system that generates a token for identity.
Cryptographic mechanism, token format, signing algorithm, claims, and key management are not specified in the current source.
Open related documentation →
Implementation details coming soon
Token format, signing, claims, and key management are not specified in the source. Do not treat this page as a cryptographic specification.
Discovery
Interoperability

### PAGE
url: https://realtimeweb.org/docs/architecture/bijective-network
also: https://realtimeweb.org/hood/architecture/bijective-network
title: Bijective network · Real Time Web

Bijective network · Real Time Web
DOCUMENTATION
Bijective network
One endpoint maps to one ghost. The relationship is addressable from both sides.
A conventional hyperlink points one way. The page you link from knows the target. The target does not have to know who pointed at it. That is enough for documents.
The Real Time Web needs a different pairing. Each participating endpoint has one corresponding ghost , and that ghost represents that one endpoint. The relationship can be addressed and maintained from both sides. Authorized updates can travel as they occur. The source calls this a Bijective Network System .
World Wide Web
Real-Time Web
Bijective, in ordinary language, means a clean one-to-one pairing that reverses. Nothing is left over. If a ghost could stand for two lamps at once, ownership of the data would stop being answerable. If two ghosts stood for one lamp, you would no longer know which stand-in was current.
Endpoint ↔ Ghost: unique bijective relationship
Why the pairing is bidirectional
In the existing Web, you retrieve a document by asking. For machines that sense and act, asking is the wrong default. A sensor should be able to notify. An actuator should be able to receive. The same relationship has to carry both directions without inventing a new integration for each pairing.
The ghost is the addressable stand-in. What the endpoint reports, the ghost can carry. What the ghost is authorized to receive, the endpoint can act on. The ghost provides identity, behavior, and context when an active connection is present.
The pairing is not a chat room of avatars. People participate in the ecosystem. A person is not a ghost. The ghost is tied to the resource.
Four layers stay independently owned
The pairing sits on Morphic Architecture Design. A change in one layer does not have to redefine the whole relationship.
Four layers. Four possible owners.
Layer Who What it does Teaching picture
L1 Infrastructure Hosting, hardware, connectivity Processing, links, energy, storage where required The roads
L2 Network and security Whoever runs addressing and trust Identity, authentication, authorization, secure communication The checkpoint
L3 Domain and application Service developer Services, linking, transformation logic The shop
L4 Resource and ownership The person, machine, or device that owns the resource Whether the data may be accessed or shared The goods, and who may use them
L1 · Infrastructure
Hosting, hardware, connectivity
Processing, links, energy, storage where required
The roads
L2 · Network and security
Whoever runs addressing and trust
Identity, authentication, authorization, secure communication
The checkpoint
L3 · Domain and application
Service developer
Services, linking, transformation logic
The shop
L4 · Resource and ownership
The person, machine, or device that owns the resource
Whether the data may be accessed or shared
The goods, and who may use them
Infrastructure, network and security, domain and application, and resource and ownership can have different owners. The company that hosts a box does not have to own the reading. The person who wrote a scheduler does not have to own the lamp. You do not have to run the network in order to decide who may see the data.
Ghost Space is the shared coordination environment around that one resource, so the four layers can observe authorized updates without one party owning the stack. See Ghost Space .
Data still waits for ownership
A bijective pairing is not an open pipe. The linking path can be complex. Data is consumed at an endpoint when the ghosts at the ends are owned by the same user, or the receiver has approved read access.
There is no centralized API or database required to build RTW services in this model. Each service works on local structures. How data was morphed is unknown outside that service. The network does not natively store the value.
Data is consumed when ownership or approved read access is present
Flows
Same owner, two endpoints
You own the lamp ghost. You also own the ghost that represents you inside the scheduler. The ends match. Live data can be consumed.
Or you morph the lamp ghost against the scheduler. That is read access, and you can take it back.
Does not flow
No match, no morph
A neighbor’s lamp is not yours. Sharing an implementation does not open the data. Without ownership or an approved morph, nothing is consumed at the endpoint.
It sits on the existing Internet
The Bijective Network System is described as backward compatible with the Internet we already have. RTW does not replace TCP, and it does not replace the World Wide Web. It adds a live, bidirectional dimension on top of and beside them.
A conventional website can still publish documents. RTW can carry the live channel beside that site. Existing devices and applications can become participants over time. The whole Internet does not have to be rebuilt.
Protocol independence is part of the same idea. The service owner chooses how a service is described. The micropage is where that description lives. This site does not publish command tables or encodings.
Architecture proposal
Several topology, naming, and protocol questions remain draft or unanswered in the source. This page states the pairing and the ownership rule. It does not invent a wire format.
Keep reading
Next in this path is Morphic services , then Data channels .
Under the hood
Want to see how live channels work? Read the blueprint →
Network topology
Blueprint

### PAGE
url: https://realtimeweb.org/docs/architecture/data-channels
also: https://realtimeweb.org/hood/architecture/data-channels
title: Data Channels · Real Time Web

Data Channels · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Data Channels
A linking path that collects live sources into one user’s local ghost.
Architecture proposal
Data channels are described in the architecture notes. Protocol details, naming, and discovery around a channel remain unanswered in the source.
A data channel is how a linking path collects live sources into a channel of data associated with one user’s ghost in a local service.
The picture in the source is ordinary. You create a service that wants temperature. Several makers already offer temperature services. You link to them. Each sensor updates its own ghost. For a given person, the readings that belong to that person gather in the data channel of their primary ghost in your service.
Linking path: data is morphed in local context
What has to be true before anything arrives
Linking is not enough. The path can be long. Each node only works on local structures. How a value was morphed is unknown outside that service.
Data is consumed at an endpoint when the ghosts at the ends are owned by the same user, or the receiver has approved read access. Only data with a valid morphed ghost is received.
Same user usually means one person and two of their endpoints. It does not mean two different people become one person because they share an implementation. Two people do not open each other’s readings by default. One of them morphs (read) or transfers (ownership).
When a service owner morphs a user’s ghost into a primary service, the data collected for that user is available in that user’s channel on the local service. The user has a presence at both ends of the value chain. The endpoint that is bijectively connected to those ghosts can consume the result.
The channel is personal
Two people can use the same service address and not receive the same values. Each listens through their own ghosts. The local model can be shared. The origin is not.
That is how the architecture avoids a central dump that every client polls. The network does not natively store the channel. A service may persist what it has been granted, in the local shape it understands. That is optional and local.
If nobody is listening, the value does not need to travel. That is a different cost from a store that answers whether or not the reading changed.
Several sources, one local shape
A channel can gather more than one maker. The receiving service still has one local model. Each incoming source is morphed to fit that model. A sensor that reports in one unit does not force every other service to change. The normalizer does the fit. If the service then changes the value after absorb, that is a materializer .
The owner of the original source can withdraw a morph. That source goes dark in the secondary channel. Other sources on the same channel can keep arriving. The primary home of the withdrawn source keeps working.
What a channel is not
It is not a public firehose. It is not a search inbox of stored events. It is not a chat room.
It is a live path, for a user who owns or has been granted the ends, into a local ghost whose service has described its own shape.
See Morphic services for primary and secondary homes, or What it can do for the temperature and room stories.
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Morphic services
Identity

### PAGE
url: https://realtimeweb.org/docs/architecture/discovery
also: https://realtimeweb.org/hood/architecture/discovery
title: Discovery · Real Time Web

Discovery · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Discovery
Distributed stack, name resolution, and protocol independence.
In MAD, the vertical communication stack layers are segregated. The stack is also distributed to the endpoint on activation. The endpoint prior to the communication does not need to contain any protocol, libraries or pre-defined program behaviour.
If an identified user owns and controls the whole stack of a domain, that user also controls ownership of allocated ghosts for endpoints connecting against that domain address space. See Domains .
Protocol independence
RTW is protocol independent. The service owner decides their own protocol. An implementation may use common Internet transports such as TCP/IP, HTTPS, and websocket, so an endpoint can connect using a native TCP connection and send or receive data. That is a possible implementation choice, not a requirement of the architecture.
Information about how data is structured lives on each micropage . This site does not publish encodings or command tables.
Name resolution
How an RTW name resolves to a network resource, how that relates to conventional DNS, and whether an existing internet domain can be attached are not answered in the current source. Those questions belong with an implementation’s naming system, not as invented protocol here.
Implementation details coming soon
A general discovery and name-resolution specification, including how RTW names relate to conventional DNS, is not provided as public copy yet.
Domains
Authentication

### PAGE
url: https://realtimeweb.org/docs/architecture/domain
also: https://realtimeweb.org/hood/architecture/domain
title: Domain and Application Layer · Real Time Web

Domain and Application Layer · Real Time Web
DOCUMENTATION
Domain and Application Layer
Domains, services, applications, and transformation logic.
The domain and application layer contains the domains, services, applications, and transformation logic that create functionality and determine how authorized data is processed.
Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
Service developers own their applications and transformation logic. Independently from the data layer, ownership of a service can be transferred to another person. The service itself is also a ghost in the application layer.
Ghost id zero is the service (application-layer ghostid). A service owner can give away the service by transferring ghost id zero to another person.
The service owner has always access to a local copy of data related to the application layer. This includes morphed data and command data.
Implementation details coming soon
Domain naming records, micropage schema language, and service transfer protocol are not specified in the current source.
Network / Security Layer
Resource / Ownership Layer

### PAGE
url: https://realtimeweb.org/docs/architecture/domains
also: https://realtimeweb.org/hood/architecture/domains
title: Domains · Real Time Web

Domains · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Domains
A domain is an address space you control, not a website URL.
Architecture proposal
Domain naming, public DNS, and how an existing name is attached remain unanswered in the source. This page states what a domain is in MAD.
What is an RTW domain?
A domain here is an address space you control. It is not “the website URL.”
If an identified user owns and controls the whole stack of a domain, that user also controls ownership of allocated ghosts for endpoints connecting against that domain address space.
Whether you need a public DNS name, can register a name through a marketplace, or can attach a domain you already own is not answered in the current source. Those are implementation and onboarding questions. They do not live on this architecture site.
MAD is a bijective network system that allows anything to be connected. Physical or virtual network resources can be connected. Even an endpoint without any implementation that is able to keep a connection alive can receive program execution and data from its ghost.
This kernelization process allows empathy devices to connect and get their intelligence or program once activated. It also enables AI agents to activate the endpoint and control the behavior remotely. The ownership of the ghost determines which ghost layer can be configured at runtime.
In practice any object can be a participant in the heterogeneous network without any library or deployment prior to connecting. The ghostID can be mapped to the mac address and there will be a bijective relationship between the object and its ghost.
See How participation works for the conceptual path, or Discovery for what remains unanswered about names.
Identity
Discovery

### PAGE
url: https://realtimeweb.org/docs/architecture/ghost-space
also: https://realtimeweb.org/hood/architecture/ghost-space
title: Ghost Space · Real Time Web

Ghost Space · Real Time Web
DOCUMENTATION
Ghost Space
Shared state between independently controlled layers and a bijective endpoint relationship.
MAD introduces a shared state model called Ghost Space.
Within Ghost Space, a Ghost is a shared-memory representation of a network resource. It provides a common state through which the four layers can observe and process authorized updates.
Each layer can maintain its own state and logic in relation to the Ghost without assuming ownership of the complete endpoint or the other layers.
Endpoint ↔ Ghost: unique bijective relationship
Bijective relationship
The actual endpoint (such as a sensor, actuator, AI agent, application, device, domain resource, or user-controlled data source) has a unique bijective relationship with its Ghost.
This means that:
The endpoint has one corresponding Ghost.
The Ghost represents one corresponding endpoint.
The relationship is uniquely addressable from both sides.
Authorized state changes can be propagated through the relationship.
Each layer can process the update according to its own role and permissions.
Ghost Space therefore functions as the shared coordination environment between infrastructure, security, applications, and resource owners. It allows these layers to cooperate around the same live network resource while remaining independently controlled.
Ghost Space is not a chat room where people’s avatars meet. The ghost is tied to a resource or endpoint, not to a human avatar.
Identity and protection
A ghost is a kind of proxy for the network resource. Ghost operates in multiple layers and can be accessed by the other stack layers at runtime. Each unique network resource is bijective connected to its own ghost. The ghost provides identity, behavior and context when an active connection is present.
Ownership across layers
A ghost is represented in all stack layers. Ownership of the ghost in the application layer belongs to the service owner. Ownership of the data layer can belong to the user after transfer of the ghostId .
Resource / Ownership Layer
Ghosts and twins

### PAGE
url: https://realtimeweb.org/docs/architecture/ghosts-and-twins
also: https://realtimeweb.org/hood/architecture/ghosts-and-twins
title: Ghosts and twins · Real Time Web

Ghosts and twins · Real Time Web
DOCUMENTATION
Ghosts and twins
A ghost is a live stand-in across MAD layers. A digital twin is usually a stored model in one place.
The word ghost is easy to misuse. In this architecture it is not a person, not an avatar, and not a cursor in a shared document. A ghost is the live stand-in for one network resource.
A digital twin is a useful nearby idea, and the source draws a line between the two. A ghost can be used to build twin-like services. It is not only a stored model of a thing.
One endpoint. One ghost. Addressable both ways.
What the ghost is
When an endpoint can participate, it is paired with a ghost. The pairing is bijective : one endpoint, one ghost. The ghost provides identity, behavior, and context when an active connection is present.
Whoever owns the ghostId owns the data at that endpoint. When a Morphic service is created, the service owner is the primary owner of allocated ghosts. After a user confirms a transfer, the user owns the data layer. The service owner keeps the application layer and may keep a local copy.
The ghost operates in more than one layer at once. Infrastructure, security, applications, and owners can each hold state in relation to the same ghost without taking the other layers. That shared coordination environment is Ghost Space .
Endpoint ↔ Ghost: unique bijective relationship
How this differs from a stored twin
A digital twin, as commonly built, is a model kept in a system whether or not the physical thing is talking. It often lives in one layer, usually the data layer, and is updated by copying readings into a store.
A ghost is not required to sit in a database when nothing is happening. The source describes a small footprint: the stand-in is there for the authorized exchange. When the connection ends, the ghost can go quiet or be removed, depending on how the service owner has set that service. Historical values are not natively persisted by the network.
The other difference is depth. A ghost can receive events up and down the MAD stack. Hosting, security, application logic, and the data owner each see the ghost in the role that belongs to their layer. A stored twin that only mirrors the reading cannot give those other parties a lawful place to act without taking the data.
Ghost and digital twin
What other layers can do
Because the ghost is shared across layers, a service owner can stop a connection to their service without owning the endpoint’s data. A security layer can handle identity without owning the application. A domain owner who controls the full stack of an address space controls ghosts allocated against that space.
None of that turns the ghost into a person. If you own a hundred sensors across several services, you control the data those services receive from your endpoints. How the values are reshaped still belongs to each service.
Transfer and read access
Two actions are easy to confuse.
Transfer moves the ghostId. The new holder confirms. After confirm, they own the data layer. That is a change of ownership.
Morphing a ghost against a secondary service grants read access and reshapes the value into that service’s local model. The original holder keeps the ghostId. The morph can be withdrawn.
A ghost can also be mapped to an identifier the object already has, such as a hardware address. The source describes that as a way to keep the bijection between the object and its stand-in. How a given implementation issues those identifiers is not specified here.
What this page will not do
This page will not describe command lists, token lifetimes, or product consoles. Those belong with an implementation. The architecture claim is smaller and stricter: one live stand-in per resource, across independently owned layers, with ownership sitting on the ghostId.
See Ghost Space for the coordination model. Next in this path is Bijective network .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Ghost Space
Morphic services

### PAGE
url: https://realtimeweb.org/docs/architecture/identity
also: https://realtimeweb.org/hood/architecture/identity
title: Identity · Real Time Web

Identity · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Identity
Addressing, ghost allocation, and optional authentication systems.
There is no centralized API or database in use when building RTW services.
How are services, devices, and AI agents identified?
At the architectural level they are identified the same way: as endpoints with one corresponding ghost. The pairing is bijective. One resource, one ghost, addressable from both sides.
A device, a sensor, an application, and an AI agent can each be an endpoint. A person participates in the ecosystem. A person is not a ghost.
A Morphic service is itself a ghost in the application layer. Ghost id zero is the service. Transferring that handle transfers the service, independent of who owns data layers on other ghosts.
How those identities are written on the wire, and how names resolve, is not specified in the current source.
When ghosts are allocated for the first time, all allocated ghosts are owned by the service owner. Once a new user has been registered to the service the service owner can transfer the ghost id to the user. When the user approves the transfer the user now controls the data layer of the specific ghost.
The service itself is also a ghost in the application layer. Independently from the data layer, ownership of the service can also be transferred to another person. There are four layers of ownership in the vertical communication stack that independently from each other can be changing ownership.
MAD has been designed using roles and responsibility patterns, so what kind of authentication system is used is optional when constructing an RTW network. Any token system that generates a token for identity can be used.
Conceptual identity path. Not a protocol specification.
01 Participant
02 Identity
03 Authentication
04 Network identity
05 Domain / space
06 Data channels
07 Real Time Web
Expandable node
Authentication
Authentication is optional in MAD. An implementation may use any token system that generates a token for identity.
Cryptographic mechanism, token format, signing algorithm, claims, and key management are not specified in the current source.
Open related documentation →
Implementation details coming soon
How services, devices, and AI agents are identified at the protocol level is not specified in the current source.
Data Channels
Domains

### PAGE
url: https://realtimeweb.org/docs/architecture/infrastructure
also: https://realtimeweb.org/hood/architecture/infrastructure
title: Infrastructure Layer · Real Time Web

Infrastructure Layer · Real Time Web
DOCUMENTATION
Infrastructure Layer
Physical or virtual infrastructure that sustains network operation.
The infrastructure layer is the physical or virtual infrastructure that provides processing, connectivity, storage capacity where required, and energy to sustain network operation.
Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
In the message example, this is the layer that operates devices, routers, network equipment, and computing resources so a communication can be transported at all.
Infrastructure providers control their infrastructure. A change at this layer does not need to redefine identity, application logic, or resource ownership.
Implementation details coming soon
Hardware profiles, node types, energy and storage requirements, and deployment topologies are not specified in the current source. Implementation details coming soon.
Morphic Architecture
Network / Security Layer

### PAGE
url: https://realtimeweb.org/docs/architecture/interoperability
also: https://realtimeweb.org/hood/architecture/interoperability
title: Interoperability · Real Time Web

Interoperability · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Interoperability
Local models, morphing along a path, and an empty endpoint that can receive a program first.
Architecture proposal
Interoperability notes in the source are still marked draft. This page stays at the architectural idea. It does not publish a schema language.
The Semantic Web has a working habit: when you link to a source, you turn that source to fit your local model. When someone later links to you, they do the same. If every service keeps that habit, the whole remains livable.
MAD uses that habit on a live path, not only on stored documents.
Linking path: data is morphed in local context
Fit the local model
To link a source and morph it so it fits the local data model is called normalizer . The receiving service keeps its own shape. The source does not have to change.
If the service then offers to change the data after the local model has been updated, that is a materializer . The change stays in local context. Other nodes do not see how it was done.
The predicate on a link is the verb in that fit. The logic belongs to the service that defined it. Domain owners keep that logic intact even as others link in. End users keep control of whether the source is available at all.
An empty endpoint can start
For endpoints and their ghosts, the source describes a further step. Kernelizer lets the endpoint receive a self-contained message before the data stream. The application-layer owner can send a program first. The data-layer stream follows. The client can build its interface without a preinstalled application.
The endpoint can therefore be distributed as an empty container. Program and data arrive later. Ownership of the ghost decides which layer may be configured at runtime.
This is also how the architecture talks about objects that have almost no stack of their own. If they can keep a connection alive and be identified, they can receive intelligence from a service. The limit is still the body of the object.
Protocol independence
RTW is protocol independent. The service owner decides their own protocol. Information about how data is structured lives on each micropage . An implementation may support more than one encoding and change format at runtime when a client with domain ownership requests it.
This site will not publish those encodings. If a service does not describe itself, others have no serious basis for linking to it.
What interoperability is not
It is not one global data model that everyone must adopt. It is not a central API. It is the rule that each service keeps its own shape, and that a live source is morphed into that shape along the path.
See Morphic services and Data channels .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Authentication
Network topology

### PAGE
url: https://realtimeweb.org/docs/architecture/morphic-services
also: https://realtimeweb.org/hood/architecture/morphic-services
title: Morphic services · Real Time Web

Morphic services · Real Time Web
DOCUMENTATION
Morphic services
An application on MAD that allocates ghosts, keeps its own shape, and can inherit a source from another home.
A Morphic service is an application-layer service on MAD. It allocates ghosts. It publishes a local data model. It can link to other services and reshape what arrives so the local model stays intact.
The name comes from biology: morphogenesis, organizing fields. In this architecture it means a system can inherit behavior by tuning into the right live channel. The source compares that to changing a radio frequency. You are not fetching a stored file. You are receiving a stream whose content is determined by your ownership and by the services on the path.
Teaching sketch of a local data model. Not a protocol specification.
Morphic service
Lamp service
An application-layer home that allocates ghosts. The service owner starts as primary owner of those ghosts.
Local model
brightness live
is_on live
The shape lives with the service. Other services morph into their own models. RTW does not require one encoding for everyone.
Primary home, secondary context
An endpoint belongs first to a primary service . It inherits that service’s local model. Sensors that leave a factory with one job still have a home they can speak to.
A secondary service is a different home. The owner morphs the ghost against it. Two things happen at once:
The secondary service receives read access. The owner can withdraw it.
The data is reshaped into the secondary service’s local model. How it was reshaped is unknown outside that service.
The sensor does not have to change. A temperature service can keep Celsius. A second service can work in another local shape. Each node only sees its own context.
Morphing grants read access and reshapes data into a local model
The object stays itself. The service supplies the context.
What the service owner keeps
When the service is created, the service owner is the primary owner of allocated ghosts. When a user registers and confirms a transfer, the user owns the data layer. The application layer stays with the service owner. The service owner may keep a local copy.
Ghost id zero is the service itself. Transferring that handle transfers the service, independent of who owns data layers on other ghosts.
The service owner also decides the protocol. RTW is described as protocol independent. The public description of the model lives on a micropage : a mini sheet for the service and its schema. If a service does not describe what it offers, other services have no serious basis for linking to it. The source treats that as a market check, not as a central registry.
Links are sentences
Services connect with links. The source uses the Semantic Web picture of a sentence: a subject, a predicate , and an object. The subject is the service and its model. The object is the source being linked. The predicate is the verb: what this service does to the incoming value so the local model stays true.
You do not need to learn a notation to use the idea. If every service fits what it links into its own shape, the next service along the path can do the same. The network as a whole stays livable. A service that keeps breaking its model will simply be linked to less.
A normalizer is that fit on the way in. A materializer is a further change after the local model has been updated. Both stay local.
Channels, not dumps
A data channel is how a linking path collects sources into one user’s local ghost. The canonical picture is temperature from several makers, gathered for one person. Only data with a valid morphed ghost is received. Both ends need a user who owns the data or has been granted read access.
The channel is personal. Two people can connect to the same service URI and receive different values, because each is listening through their own ghosts. The structure can be the same. The origin is not.
Linking path: data is morphed in local context
What can change at runtime
The local model is not required to be frozen for the life of a connection. The source describes services that can change structure while clients remain connected. The connection point stays. The shape of what arrives can change.
That is a large claim and a draft-heavy area. This page will not turn it into a click path. The architectural point is that identity and relationship can remain while access rules and transformation logic evolve. See Interoperability .
What this is not
A Morphic service is not a shared document everyone is editing. It is not a paste that matches formatting. It is not an API you must adopt before you can speak.
It is an application on four independently owned layers, with ghosts for the endpoints that use it, and links that reshape live sources into a local model the owner of that service controls.
Keep reading
Next in this path is Data channels .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Ghosts and twins
Data Channels

### PAGE
url: https://realtimeweb.org/docs/architecture/network
also: https://realtimeweb.org/hood/architecture/network
title: Network and Security Layer · Real Time Web

Network and Security Layer · Real Time Web
DOCUMENTATION
Network and Security Layer
Addressing, identity, authentication, authorization, trust, and secure communication.
The network and security layer contains the mechanisms responsible for addressing, identity, authentication, authorization, trust, and secure communication.
Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
Network and security providers manage connectivity and trust. MAD has been designed using roles and responsibility patterns, so what kind of authentication system is used is optional when constructing an RTW network.
The MAD network does not natively persist data into databases or filesystems. It is designed as a distributed machine network. The network is tokenized and is limited to the system that issues the token and how this is mapped to the user or network resource. Any token system that generates a token for identity can be used.
The security and trust model, including how access is withdrawn, is written under Authentication .
Implementation details coming soon
Signing algorithms, key management, and a canonical token format are not specified here. Architecture proposal only.
Infrastructure Layer
Domain / Application Layer

### PAGE
url: https://realtimeweb.org/docs/architecture/resource
also: https://realtimeweb.org/hood/architecture/resource
title: Resource and Ownership Layer · Real Time Web

Resource and Ownership Layer · Real Time Web
DOCUMENTATION
Resource and Ownership Layer
Who generates a resource and who controls whether it may be accessed.
The resource and ownership layer is the person, organization, machine, or device that generates or owns the resource and controls whether it may be accessed or shared.
Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
In Real Time Web, data ownership is given by the ghostId . Whoever owns the ghostId also owns the data at this endpoint.
When a new Morphic service is created, the owner of the service becomes the primary owner of all ghosts that are allocated on the service. When a user is registered for the service, the service owner transfers the ghostId to the user. When the user confirms ownership, the ghost data layer belongs to the user. The application layer on the ghost still belongs to the service owner.
The data source is owned by the user that controls the endpoint and has registered it against the endpoint ghost. The ghost can be transferred to another person. By morphing the ghost against a secondary service the owner gives read access to the service provider. The read access can anytime be withdrawn by the owner.
Where data is stored
Data is not natively stored in the network. Based on how the linking relationship is set up between services, data is dynamically morphed into local data models along the linking path. If data has been shared with a service, the service owner may persist it in the local context they receive.
For data to pass through the linking path and be consumed at an endpoint, the sender and receiver ghosts must belong to a user who owns the data or has been granted read access. The RTW network natively does not store data, but a service provider may connect a database to their local ghosts.
Service providers and trust
A service provider that gains read access to several users’ data may decide to share that data with other users. The service provider needs to be trusted and responsible for how they use the data, even when each user approved the morph individually.
Privacy and sovereignty
Supporting privacy and sovereignty means the user can control who has access to the data source, and that data is not persisted in the network space unless the user has agreed to it. Ownership of a ghost and a direct path to the original source lets the user morph that ghost into a secondary service and share data with them.
Domain / Application Layer
Ghost Space

### PAGE
url: https://realtimeweb.org/docs/architecture/topology
also: https://realtimeweb.org/hood/architecture/topology
title: Network topology · Real Time Web

Network topology · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Network topology
Data channels built along a linking path. Each node only sees local context.
Architecture proposal
Network topology is described in the architecture notes and is still marked draft. This page states that model. It does not invent a wire format or a central graph.
The horizontal topology in MAD is not a request-and-response tree, and it is not a stored Linked Data graph that everyone queries. It is a linking path . Sources are collected into a data channel . Along that path, data is morphed into each service’s local model.
Each service or node operates on local data structures. It can persist and access data only in local context. How a value was morphed is unknown outside that service or domain.
Linking path: data is morphed in local context
No central API in the middle
There is no centralized API or database required to build RTW services in this model. You construct a link from your local service against a secondary service whose data structure has been publicly announced. The path can be long. The network does not natively store the channel.
Data is consumed at an endpoint when the ghosts at the ends are owned by the same user, or the receiver has approved read access. Same user usually means one person and two of their endpoints. Two different people do not open each other’s data because they share an implementation.
Why traffic does not have to be a dump
If nobody is listening, the value does not need to travel. That is a different cost from a store that answers whether or not the reading changed.
RTW is designed to keep data associated with the resource and domain where it was generated, rather than copying every reading into a centrally controlled platform. Authorized updates can move as they occur, for the user instance that owns or has been granted the ends.
This is the architectural answer to unnecessary traffic in the source notes. It is not a congestion-control specification.
Keep reading
See Data channels for the temperature picture, or Bijective network for the pairing the path sits on.
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Interoperability
Bijective network

### PAGE
url: https://realtimeweb.org/docs/architecture
also: https://realtimeweb.org/hood/architecture
title: Morphic Architecture Design · Real Time Web

Morphic Architecture Design · Real Time Web
DOCUMENTATION
Morphic Architecture Design
RTW is based on MAD, an architectural model with four independently controlled layers.
The Real-Time Web is based on Morphic Architecture Design (MAD), an architectural model first introduced by technology inventor Paal Kristian Levang in 2008.
Like the World Wide Web, RTW uses semantic principles to describe resources and their relationships. However, RTW extends beyond the document and application layer by coordinating several concurrent layers of the communication architecture.
MAD defines a minimum of four logical ownership and operational layers.
Morphic Architecture Design: four logical layers
L1 Infrastructure Layer
L2 Network and Security Layer
Purpose
Mechanisms for addressing, identity, authentication, authorization, trust, and secure communication.
Components
Identity, trust, addressing, and communication security.
Implementation details coming soon. Related page: Network and Security Layer
L3 Domain and Application Layer
L4 Resource and Ownership Layer
Independent control
In the conventional Web, standards primarily define how resources are identified, described, requested, and presented at the Web and application layers. The underlying networking infrastructure is provided through technologies and standards operated by hardware manufacturers, telecommunications providers, Internet service providers, and network operators.
Identity, sessions, payments, and access control are then frequently implemented separately by each application or domain. The result is millions of independent login systems, user accounts, payment integrations, and proprietary trust mechanisms.
MAD proposes a multi-layer network stack in which the four logical layers can be configured and updated independently at runtime.
A change in one layer does not need to redefine the entire network relationship. Instead, the semantics, data structure, access rules, and transformation logic associated with a resource can evolve while its fundamental network identity and relationships remain intact.
This design allows different participants to control their respective layers:
Infrastructure providers control their infrastructure.
Network and security providers manage connectivity and trust.
Service developers own their applications and transformation logic.
Resource owners control access to their data and endpoints.
The objective is to preserve ownership and privacy at each layer without preventing the other participants from performing the functions necessary to deliver and transform data.
A simple example
Consider sending a message to a friend. All four layers participate, but they do not necessarily have the same owner.
Layer Independent participant Role in a message
Infrastructure Hardware / connectivity provider Operate devices and transport the message
Network / security Network operator Identify, authenticate, and protect the communication
Domain / application Application developer Construct, process, send, and receive the message
Resource / ownership End user Create the message and decide to share it
Infrastructure
Hardware / connectivity provider
Operate devices and transport the message
Network / security
Network operator
Identify, authenticate, and protect the communication
Domain / application
Application developer
Construct, process, send, and receive the message
Resource / ownership
End user
Create the message and decide to share it
Ghost Space
MAD introduces a shared state model called Ghost Space. The actual endpoint has a unique bijective relationship with its Ghost. See Ghost Space , Ghosts and twins , and Bijective network .
A Morphic service is the application-layer home that allocates those ghosts. See Morphic services .
The service owner decides the protocol. RTW is protocol independent. The public description of a service lives on a micropage. See Interoperability .
Endpoint ↔ Ghost: unique bijective relationship
Promise
Infrastructure Layer

### PAGE
url: https://realtimeweb.org/docs/implementation/blueprint
also: https://realtimeweb.org/hood/implementation/blueprint
title: Blueprint · Real Time Web

Blueprint
Live data channels, user-controlled sources, and coexistence with the World Wide Web.
A framework for the Internet of Everything
The Real-Time Web is intended to provide a more flexible way to build Internet of Everything systems.
Today, sensor data is commonly collected through proprietary APIs and middleware before being copied into databases or cloud platforms. Applications must then request the stored data through platform-specific interfaces. This creates additional infrastructure, repeated integrations, duplicated data, and dependency on intermediaries.
Direct live channels
RTW proposes an alternative. Live data channels can connect the original data source directly to the appropriate web service, application, AI agent, device, or web page for a particular user instance.
Figure 3-1 concept: Bijective Network System (redrawn from source description)
Figure 3-1, as described in the source, shows the Real-Time Web connecting the digital Web to the physical world through a Bijective Network System. Dynamic data channels connect Internet of Everything resources directly to the appropriate service, application, or web page for a specific user instance. The resulting network operates concurrently with the World Wide Web, adding live, bidirectional communication.
The Real-Time Web does not need to replace the World Wide Web. It can operate alongside it in symbiosis. The conventional Web remains well suited to documents, published information, and media, while RTW adds a dynamic network for live resources, machine interaction, and continuously changing data.
Bidirectional addressing
Each participating endpoint has a unique corresponding representation in the network. Authorized updates can be distributed as they occur, rather than being retrieved only through a request.
Data can remain associated with its original source. Network relationships can persist across participating services. Data access and transformation logic can be controlled separately.
Four layers in every exchange
Even a simple action like sending a message involves all four MAD layers, often with different owners. See Morphic Architecture .
Layer Independent participant Role in a message
Infrastructure Hardware / connectivity provider Operate devices and transport the message
Network / security Network operator Identify, authenticate, and protect the communication
Domain / application Application developer Construct, process, send, and receive the message
Resource / ownership End user Create the message and decide to share it
Infrastructure
Hardware / connectivity provider
Operate devices and transport the message
Network / security
Network operator
Identify, authenticate, and protect the communication
Domain / application
Application developer
Construct, process, send, and receive the message
Resource / ownership
End user
Create the message and decide to share it
Shared state
MAD introduces Ghost Space: a shared-memory representation of a network resource through which infrastructure, security, applications, and owners can cooperate without one party owning the entire stack. See Ghost Space .
Endpoint ↔ Ghost: unique bijective relationship
How participation works
Understanding the architecture is not the same as running a live service. Ownership, identity, and access still follow MAD: a domain is an address space, a ghost stands in for one endpoint, and morphing grants read access that can be withdrawn.
Next in this path is Synx , then Morph Space .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Bijective network
Protocol Overview

### PAGE
url: https://realtimeweb.org/docs/implementation/dictionary
also: https://realtimeweb.org/hood/implementation/dictionary
title: Dictionary · Real Time Web

Dictionary
Shared RTW terminology drawn from the source.
A shared terminology is the first recommended implementation step in the source. Terms below are limited to language that already appears there.
Term Meaning
Real-Time Web (RTW) A framework and network architecture for connecting live physical and virtual resources across the Internet.
Morphic Architecture Design (MAD) Architectural model introduced by Paal Kristian Levang in 2008. RTW is based on MAD and coordinates at least four logical ownership and operational layers.
Morphic service An application-layer service on MAD. When it is created, the service owner is the primary owner of allocated ghosts. After a user confirms a transfer, the user owns the data layer; the service owner keeps the application layer.
Domain An address space in the network. If an identified user owns and controls the whole stack of a domain, that user controls allocated ghosts for endpoints connecting against that address space.
Ghost A shared-memory representation of a network resource. Each unique network resource is bijectively connected to its own ghost.
Ghost Space Shared coordination environment through which the four layers can observe and process authorized updates around the same live resource.
Bijective relationship The endpoint has one corresponding Ghost, and the Ghost represents one corresponding endpoint. The relationship is uniquely addressable from both sides.
Data channel A way to describe how a linking path collects data sources into a channel of data associated with a user's ghost in a local service.
Morphing Transforming data along the linking path to fit a local data model. Each service operates only on local data structures. Morphing a ghost into a secondary service also grants read access that can be withdrawn.
Normalizer To link a data source and morph the data to fit the local data model.
Materializer If a service offers to make changes to the data after the local data model has been updated.
Kernelizer Allows an endpoint to receive a self-contained message before the data stream, so program and interface can be built without a preinstalled client.
Micropage A mini description of a service and its data model. Service providers describe their own data schema availability here.
ghostId Ownership of data at an endpoint is given by the ghostId. Whoever owns the ghostId owns the data at that endpoint.
Ghost id zero The service (application-layer ghostid). Transferring ghost id zero transfers the service itself.
Heterogeneous network A network not controlled by a single entity. It evolves as independent participants connect and manage their own domains and services.
Endpoint The actual network resource that participates: a sensor, actuator, application, device, domain resource, AI agent, or a source you control. The ghost is tied to the resource, not to a person.
Bijective Network System (BiNS) The network model behind RTW. Each participating endpoint has one corresponding ghost, uniquely addressable from both sides.
Primary service The Morphic service an endpoint belongs to first. The endpoint inherits that service’s local data model.
Secondary service A service that receives a morphed ghost. The owner grants read access. The data is reshaped into this service’s local model and can be withdrawn.
Linking path The chain of services that collect and reshape live sources. Each node only sees its own local context.
Internet of Everything Physical devices, virtual resources, software services, AI agents, sensors, actuators, and people participating in the same connected ecosystem.
Data and information Data is the live value before it is stored. Once written into a file or database it becomes information: historical, structured, retrieved on request.
Ghost and digital twin A digital twin is usually a stored model of a thing. A ghost is a live stand-in for one endpoint and operates across MAD layers.
Predicate In a link, the predicate is the verb: what the service does with the incoming source so the result fits the local model.
Real-Time Web (RTW)
A framework and network architecture for connecting live physical and virtual resources across the Internet.
Morphic Architecture Design (MAD)
Architectural model introduced by Paal Kristian Levang in 2008. RTW is based on MAD and coordinates at least four logical ownership and operational layers.
Morphic service
An application-layer service on MAD. When it is created, the service owner is the primary owner of allocated ghosts. After a user confirms a transfer, the user owns the data layer; the service owner keeps the application layer.
Domain
An address space in the network. If an identified user owns and controls the whole stack of a domain, that user controls allocated ghosts for endpoints connecting against that address space.
Ghost
A shared-memory representation of a network resource. Each unique network resource is bijectively connected to its own ghost.
Ghost Space
Shared coordination environment through which the four layers can observe and process authorized updates around the same live resource.
Bijective relationship
The endpoint has one corresponding Ghost, and the Ghost represents one corresponding endpoint. The relationship is uniquely addressable from both sides.
Data channel
A way to describe how a linking path collects data sources into a channel of data associated with a user's ghost in a local service.
Morphing
Transforming data along the linking path to fit a local data model. Each service operates only on local data structures. Morphing a ghost into a secondary service also grants read access that can be withdrawn.
Normalizer
To link a data source and morph the data to fit the local data model.
Materializer
If a service offers to make changes to the data after the local data model has been updated.
Kernelizer
Allows an endpoint to receive a self-contained message before the data stream, so program and interface can be built without a preinstalled client.
Micropage
A mini description of a service and its data model. Service providers describe their own data schema availability here.
ghostId
Ownership of data at an endpoint is given by the ghostId. Whoever owns the ghostId owns the data at that endpoint.
Ghost id zero
The service (application-layer ghostid). Transferring ghost id zero transfers the service itself.
Heterogeneous network
A network not controlled by a single entity. It evolves as independent participants connect and manage their own domains and services.
Endpoint
The actual network resource that participates: a sensor, actuator, application, device, domain resource, AI agent, or a source you control. The ghost is tied to the resource, not to a person.
Bijective Network System (BiNS)
The network model behind RTW. Each participating endpoint has one corresponding ghost, uniquely addressable from both sides.
Primary service
The Morphic service an endpoint belongs to first. The endpoint inherits that service’s local data model.
Secondary service
A service that receives a morphed ghost. The owner grants read access. The data is reshaped into this service’s local model and can be withdrawn.
Linking path
The chain of services that collect and reshape live sources. Each node only sees its own local context.
Internet of Everything
Physical devices, virtual resources, software services, AI agents, sensors, actuators, and people participating in the same connected ecosystem.
Data and information
Data is the live value before it is stored. Once written into a file or database it becomes information: historical, structured, retrieved on request.
Ghost and digital twin
A digital twin is usually a stored model of a thing. A ghost is a live stand-in for one endpoint and operates across MAD layers.
Predicate
In a link, the predicate is the verb: what the service does with the incoming source so the result fits the local model.
Data channels specification
FAQ

### PAGE
url: https://realtimeweb.org/docs/implementation/skalle
also: https://realtimeweb.org/hood/implementation/skalle
title: Skalle · Real Time Web

Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
Skalle
Skalle is named as a party planning an RTW implementation. Detail is not in the public source yet.
Architecture proposal
Skalle is listed here because it is planning an implementation. The public source used for this site does not yet describe Skalle's product, protocol, or screens. This page does not invent them.
Skalle is a party planning to implement MAD or the Real Time Web. That is all this site can state without leaving the written source.
Skalle would be one more independent party, not a replacement for the architecture.
When a written description exists in the source, this page can be expanded. Until then, treat Skalle as a name on the implementation map, not as a specified product.
See How it works .
Morph Space
Reference Implementations

### PAGE
url: https://realtimeweb.org/docs/implementation/synx
also: https://realtimeweb.org/hood/implementation/synx
title: Synx · Real Time Web

Synx
High-level note on Synx as a known toolchain for RTW services.
Synx is a known set of tools used to configure, administer, secure, and maintain RTW services. In the source, the company is Synx. The tools are not the Real Time Web itself.
MAD treats authentication as optional. An implementation may use any token system that issues identity. Synx is one known toolchain in that layer. It is not the only possible one.
Token formats, refresh rules, BIOS, protocols, APIs, and screens belong in Synx documentation. A service can be built on MAD without using Synx.
See also Morph Space and How it works .
Technical Resources
Morph Space

### PAGE
url: https://realtimeweb.org/docs/introduction/data-and-information
also: https://realtimeweb.org/hood/introduction/data-and-information
title: Data and information · Real Time Web

Data and information · Real Time Web
DOCUMENTATION
Data and information
The World Wide Web is strong at stored information. The Real Time Web is aimed at live data from the source.
There is a distinction this architecture depends on. If you treat the two words as synonyms, the rest of the model will look like a faster website. It is not.
Information is structured historical data. It has already been written into a file, a page, or a database. A person can retrieve it later, at a human pace, and read it in a chosen context. That is what the World Wide Web does well. You ask for a document. A copy comes back. The page you read may have been assembled from many underlying sources. Sometimes the owner of a page does not know what you are looking at. That is part of the beauty of the existing Web.
Data , in this architecture, is the live value before it is stored. It exists at the source. A temperature reading that has not yet been written down is data. The same reading, copied into a table and requested an hour later, is information. Machines that act on a changing world need the first. People who look things up need the second.
Information
Live data
Why the existing Web stops at information
A hyperlink is a pointer toward stored content: text, images, documents, video. Anyone can link to the past, the present, and the future of that content without installing software or agreeing a session. That is why the World Wide Web became the largest information network in the world.
When you want the value as it changes, the usual answer is a custom interface. You have to know who you are talking to. You miss the underlying sources that a hyperlink would have followed. Each pairing often copies the value into another store. After a few hops, several systems hold a version of the same reading, and it is no longer obvious who has the freshest one. Context decides that, and context is what gets lost when the value is copied away from the source.
The Real Time Web does not ask the World Wide Web to do that job. It sits beside it. Documents stay. Live sources get their own kind of relationship.
Live data stays with the source
RTW is designed so that a value remains associated with the resource and domain where it was generated. The owner decides whether the resource is available, who may use it, and under which conditions. Applications may process, transform, and combine authorized data into new contexts. The application provider controls that transformation. The owner of the source keeps control of access.
The network itself does not natively store data. A service may attach a database to its local ghosts after it has received a morph. That local copy is the service’s own context. It is not a required central store in the middle of the path.
This is why the architecture can talk about privacy without adding a product policy on top. If the network does not persist the value, there is less to take from the middle. Persistence is a choice made by a service that has already been granted access, in the shape that service understands.
Data moves when someone is listening
A linking path can be long. Each service on that path works only on its local structures. How the value was reshaped is unknown outside that service. The path describes the relationship. It does not, by itself, move anything.
Data is consumed at an endpoint when the ghosts at the ends are owned by the same user, or the receiver has approved read access. Same user usually means one person and two of their endpoints: a sensor and a display, a fridge and a list, a lamp and a scheduler. It does not mean two different people are treated as one.
If nobody is listening, the value does not need to travel. That is a different load from a store that must answer every request whether or not the reading has changed.
Historical data can become live again
The source is not only a sensor. A store of older values can generate new data when something processes it. An analytic service that produces a fresh result from earlier input is itself a live source. The architecture still treats that result as data at the moment it is produced. The older table remains information.
What matters is origin. If you cannot identify the source, you cannot grant access to it or withdraw that access. Copies without origin lose value in a machine network because nobody can say which one is current.
What this distinction is for
Humans need information. We cannot process a raw stream at machine speed, so we structure it and look it up. Machines that coordinate with the physical world need the value while it is still data. The World Wide Web already serves the first need. The Real Time Web is the architecture proposed for the second.
The lamp walkthrough is in the journal Two webs . Next in this path is What it can do .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Concept
What it can do

### PAGE
url: https://realtimeweb.org/docs/introduction/how-it-works
also: https://realtimeweb.org/hood/introduction/how-it-works
title: How it works · Real Time Web

How it works · Real Time Web
DOCUMENTATION
How it works
Live data channels, user-controlled sources, and coexistence with the World Wide Web.
A framework for the Internet of Everything
The Real-Time Web is intended to provide a more flexible way to build Internet of Everything systems.
Today, sensor data is commonly collected through proprietary APIs and middleware before being copied into databases or cloud platforms. Applications must then request the stored data through platform-specific interfaces. This creates additional infrastructure, repeated integrations, duplicated data, and dependency on intermediaries.
Direct live channels
RTW proposes an alternative. Live data channels can connect the original data source directly to the appropriate web service, application, AI agent, device, or web page for a particular user instance.
Figure 3-1 concept: Bijective Network System (redrawn from source description)
Figure 3-1, as described in the source, shows the Real-Time Web connecting the digital Web to the physical world through a Bijective Network System. Dynamic data channels connect Internet of Everything resources directly to the appropriate service, application, or web page for a specific user instance. The resulting network operates concurrently with the World Wide Web, adding live, bidirectional communication.
The Real-Time Web does not need to replace the World Wide Web. It can operate alongside it in symbiosis. The conventional Web remains well suited to documents, published information, and media, while RTW adds a dynamic network for live resources, machine interaction, and continuously changing data.
Bidirectional addressing
Each participating endpoint has a unique corresponding representation in the network. Authorized updates can be distributed as they occur, rather than being retrieved only through a request.
Data can remain associated with its original source. Network relationships can persist across participating services. Data access and transformation logic can be controlled separately.
Four layers in every exchange
Even a simple action like sending a message involves all four MAD layers, often with different owners. See Morphic Architecture .
Layer Independent participant Role in a message
Infrastructure Hardware / connectivity provider Operate devices and transport the message
Network / security Network operator Identify, authenticate, and protect the communication
Domain / application Application developer Construct, process, send, and receive the message
Resource / ownership End user Create the message and decide to share it
Infrastructure
Hardware / connectivity provider
Operate devices and transport the message
Network / security
Network operator
Identify, authenticate, and protect the communication
Domain / application
Application developer
Construct, process, send, and receive the message
Resource / ownership
End user
Create the message and decide to share it
Shared state
MAD introduces Ghost Space: a shared-memory representation of a network resource through which infrastructure, security, applications, and owners can cooperate without one party owning the entire stack. See Ghost Space .
Endpoint ↔ Ghost: unique bijective relationship
How participation works
Understanding the architecture is not the same as running a live service. Ownership, identity, and access still follow MAD: a domain is an address space, a ghost stands in for one endpoint, and morphing grants read access that can be withdrawn.
Next in this path is Vision and principles , then How participation works .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
What it can do
Vision and principles

### PAGE
url: https://realtimeweb.org/docs/introduction/onboarding
also: https://realtimeweb.org/hood/introduction/onboarding
title: How participation works · Real Time Web

How participation works · Real Time Web
DOCUMENTATION
Architecture proposal
Marked as draft in the source. Needs team review before publishing as final copy.
How participation works
How identity, domains, ghost ownership, and morphing fit together in MAD. Conceptual only.
RealTimeWeb.org is a standalone nonprofit site. It explains what the Real Time Web is, why it exists, and introduces Morphic Architecture Design (MAD).
The site is independent. The idea can be built by more than one party.
Architecture proposal
This page maps the architectural path that is written. It does not invent screens, forms, vendors, or timing.
This page maps how identity, a domain, a ghost, and a morph fit together. The path is architectural. Screens and timing are still open.
How participation works in the architecture. Conceptual. Not a product onboarding guide.
01 Understand the architecture
02 Establish a network identity
03 Work inside a domain
04 Receive and confirm a ghost
05 Grant or withdraw access
06 Implement independently
Real Time Web
Understand the architecture
RTW is the network model. Start with the principles, the layers, and who owns what.
Open related documentation →
What happens, in order
1. Read the architecture
Real Time Web is a network concept and architecture. Use this documentation to learn MAD, Ghost Space, and ownership layers. Nothing here creates an account.
2. Establish a network identity
A participant needs an identity so they can be addressed in the network. How identifiers are issued is implementation-specific.
MAD treats the authentication system as optional when constructing an RTW network. Any token system that generates a token for identity can be used.
3. Work inside a domain
If an identified user owns and controls the whole stack of a domain, that user also controls ownership of allocated ghosts for endpoints connecting against that domain address space.
A domain here is an address space, not a marketing website. Whether a public DNS name is required, and how names are registered, is not specified in the current source.
4. Confirm ghost ownership
When a new Morphic service is created, the service owner becomes the primary owner of all ghosts allocated on the service. When a user registers for the service, the service owner transfers the ghostid to the user. When the user confirms ownership, the ghost data layer belongs to the user. The application layer on the ghost still belongs to the service owner. The service owner has access to a local copy of the data.
The data source is owned by the user that controls the endpoint and has registered it against the endpoint ghost. The ghost can be transferred to another person.
5. Share live data, then take it back
By morphing the ghost against a secondary service, the owner gives read access to the service provider. The read access can be withdrawn at any time.
Data is not natively stored in the RTW network. It is morphed into local data models along the linking path. For data to be consumed at an endpoint, ownership of sender and receiver ghosts must belong to a user who owns or has read access to the data.
6. Implement independently
RTW is protocol independent: the service owner decides their own protocol. More than one party can build on MAD.
What this site is for
What this site covers. Implementations are independent.
What
Real Time Web
A network architecture for live bidirectional resource relationships
Understand the idea
Why
Ownership of live data
Keep data with its source instead of copying it into platforms
Understand the problem
MAD
Morphic Architecture Design
Four independently owned layers, introduced in 2008
Understand the blueprint
Conceptual questions stay on RealTimeWeb.org. The site is a public explanation of the architecture.
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Vision and principles
The Internet of tomorrow

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/audience
also: https://realtimeweb.org/hood/introduction/tomorrow/audience
title: Target Audience · Real Time Web

Target Audience · Real Time Web
DOCUMENTATION
Target Audience
Settlers chasing new opportunities
Metaphorically speaking the Real Time Web is for settlers chasing new opportunities. We use this image to describe who we are here for and what we believe to be their shared mindset.
To begin with the Real Time Web is an idea and a potential. But there is more: it is proven technology, that through increasing application will evolve into a new technological universe and even multiply. It means that the first ones to populate this early universe creatively, can be seen as settlers.
We identify settlers as someone willing to take personal risk to achieve a greater good, or to think outside the box, to gain an advantage. They see opportunities in being a first mover, to position themselves in a future they are eager to turn into reality.
Their motivation can be:
Personal: they wish to create something for themselves
Social or business related: they wish to create value for others
This could have been the story of the Web itself or America. From what we know about the demand in the world today concerning Internet of Things/Everything and smart/intelligent solutions, we believe the Real Time Web is a candidate to a similar development.
In business strategy terminology the Real Time Web is a Blue Ocean: an unexplored area with great potential for true innovation. It's a space where newcomers can challenge and disrupt the current paradigm, and at the same time, an occasion where the establishment can reinvent themselves.
Our ecosystem is available for anyone to use from the largest corporations to teen innovators, and everything in between. Across categories, we are for the people who wished they were Web pioneers or early publishers in App Store.
Keeping in mind that we are after entrepreneurial spirits, we describe a few segments that will play important roles in the time ahead:
Developers
Since we are new, developers need to learn about how we can improve their productivity and creativity. No matter the context they work in, they would benefit from understanding the implications of the Real Time Web, both from a technological and a business point of view.
Documentation, performance, a strong community and a long term perspective are important assets to a developer. The Real Time Web may strengthen the position of the developer, inside a company or independently.
Developers are important also because they recommend management what tools and methodology to use, to get the job best done.
Partners
“Partner” is a wide term, but it refers to educational institutions, direct customers, consortiums, seminars and consultancies, ready to apply the Real Time Web in their context.
At an early stage we are ready to get others up and running, to supply successful cases and gain valuable experience. Although developers do a lot of the technical work, it is essential that management and whole organizations and authorities, think of Real Time Web as a place to look for solutions and add value.
Personality
Position

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/concept
also: https://realtimeweb.org/hood/introduction/tomorrow/concept
title: Brand Concept · Real Time Web

Brand Concept · Real Time Web
DOCUMENTATION
Brand Concept
Make amazing things together
The story about the Real Time Web is about facilitating creativity through a global network. Our ecosystem fundamentally lower the technological and economical threshold to innovate. The result is massive business opportunities and real life problem solving.
The driving force behind the Real Time Web will be the increasing demand to connect the physical and virtual world. We address the same kind of creativity that Minecraft has people invest in their virtual worlds. Only in our case, the creativity will successively impact the physical world.
In our safe environment, making sure everyone get their share, we encourage people to collaborate, test their ideas, develop applications and work on each others accomplishments.
Worth keeping in mind, is that although the potential and our belief in the Real Time Web is unlimited, its success depend on these simple insights:
The creators must find out we exist and believe that we are the future.
Individuals need to realize we represent the biggest potential for them, and why it is true.
We enable and develop a platform/an ecosystem; it's the creativity of our users that generates value.
We are excited to see where the creative community of the world will take the Real Time Web. After all, the network will expand through individuals and teams, passionate to make amazing things together.
Why Real Time Web?
Data and information

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/mission
also: https://realtimeweb.org/hood/introduction/tomorrow/mission
title: Mission · Real Time Web

Mission · Real Time Web
DOCUMENTATION
Mission
Enable an open ecosystem for the Real Time Web, an intelligent network that will continuously evolve
Through our technology, business model and philosophy we enable an open ecosystem for the Real Time Web (RTW): an intelligent network that will continuously evolve.
The ecosystem consists of network infrastructure, software and objects needed to efficiently manage and connect the physical world to the virtual world, and vice versa in real time.
The Real Time Web has potential to become the standard of Internet of Things/Everything. Things have already been connected to the Web for decades. With the Real Time Web we provide a universal and streamlined way of connecting things, intended to boost innovation everywhere and to support the world's creative economy.
With the Real Time Web one can easily link to things, in the same way as we already link to files and computers on the Web.
The more applications developed for the Real Time Web, the more the network grows, and the more resources will be available for further development.
Vision
Values

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/personality
also: https://realtimeweb.org/hood/introduction/tomorrow/personality
title: Brand Personality · Real Time Web

Brand Personality · Real Time Web
DOCUMENTATION
Brand Personality
An informal visionary
Face to face, or by means of communication, Real Time Web has the appearance of an informal visionary. The company has clear ideas and solutions for bringing the Web to another level. However the focus is here and now, on what steps to take next and how everyone may take part.
If Real Time Web was a person, the following characteristics would apply:
Open
We emit a welcoming and including attitude. By being transparent, we build trust, which is the core of our network. Our network let everyone collaborate and contribute. After all, the network consists of individual entities, investing their time, money and creative resources.
Creative
The Real Time Web is all about creating value and solving problems better. It should be obvious that we provide a treasures toolbox for creative spirits everywhere. We are a hub, that facilitates and displays what is possible, to inspire further development.
Generous
People understand that they get the most from developing in the sphere of Real Time Web. We ensure the creators maintain full ownership of what they make.
Values
Audience

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/position
also: https://realtimeweb.org/hood/introduction/tomorrow/position
title: Position · Real Time Web

Position · Real Time Web
DOCUMENTATION
Position
Universal building blocks
Real Time Web operates in an emerging competitive market. It means that there are several vendors suggesting to solve a similar problem, in different ways.
The position we aim for is: Universal building blocks.
To our knowledge nobody else can offer the same level of versatility or ability to build on each others applications.
Audience
Promise

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/promise
also: https://realtimeweb.org/hood/introduction/tomorrow/promise
title: Brand Promise · Real Time Web

Brand Promise · Real Time Web
DOCUMENTATION
Brand Promise
We let anyone connect anything to the present
Unlike traditional or alternative methods of connecting things and devices to the Web, by means of APIs and middleware with all its limitations, we let anyone connect anything to the present, through bi-directional linking.
This is a whole new invention, which enable a shared, user friendly architecture for real time connection of all things, physical and virtual.
Whereas the Web is basically designed to collect, store and transmit linked data in a network, the Real Time Web is intrinsically a network designed to process the virtual and physical present.
Just like mathematics lacked a concept of zero for a long time, the Web has lacked an elaborate concept of “Now”. The Real Time Web does not store information, but it provides real time data within itself. The data can be accessed, managed and stored through the Web.
The Real Time Web can operate as many instances interconnected with or detached from the Web, on a wide range of carriers.
Position
Morphic Architecture

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/proof
also: https://realtimeweb.org/hood/introduction/tomorrow/proof
title: Brand Proof · Real Time Web

Brand Proof · Real Time Web
DOCUMENTATION
Brand Proof
Endless digital physical innovation
The reason why we can let anyone connect anything to the present, is that our ecosystem enables endless digital physical innovation.
We present four key features, all reasons to choose and commit to the Real Time Web:
1. Shared global marketplace
From concepts like App Store and Google Play, we have learned that developers and manufacturers will invest their creativity and resources where they recognize a favorable infrastructure.
We combine the strengths of the open source community with the incentive of private ownership. Our concern is the opportunities it presents to each creator, and the work they bring into the world.
When they can all interact within the same framework and build on each others applications, we can hardly imagine the impact as the network effect gains traction.
2. Security by design
With the increasing omnipresence of information technology and the profound role it plays in society, security is key priority.
The foundation of the Real Time Web is developed by security experts with military background and standards. Precautions have been made to resist hacking and surveillance, to respect privacy and ownership, as well as safeguard transactions within the network.
3. Ultra compatible
Based on common RF specification for wireless sensor networking, and a wide protocol support, the Real Time Web is highly versatile and extremely redundant.
The Real Time Web works as the ever expanding intersection between past, present and future applications.
The technology is backwards compatible with the Web (WWW, as we know it), and can operate in intranet environments.
The link to future applications is particularly innovative, as the ecosystem enables the network to define a need, which encourage others to provide a required data or application.
4. Less custom integration
Bidirectional linking reduces the need to build a new API and middleware stack for every pairing. That is an architecture claim, not a price list.
This site does not sell access, publish plans, or price the Real Time Web. Ownership of what people create stays with them.
Governance
Version History

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/values
also: https://realtimeweb.org/hood/introduction/tomorrow/values
title: Values · Real Time Web

Values · Real Time Web
DOCUMENTATION
Values
Empower good forces
Everything we do is about empowering good forces. By good forces we mean people, companies and organizations who are passionate about what they do, considerate towards others and create something of real value. The opposite would be exploitive, cynical, greedy, anti-social and so on.
Core values
Reciprocity
We depend on each other and the world around us. What we give, somehow comes back to us. By responding to positive actions with positive actions, we create a friendly atmosphere around ourselves and what we do. This is a universal social principle, inherent in our company as well as in our technology.
Simplicity
Because we are engaged in complex matters, we recognize simplification to be fundamental. Through simplicity we make things possible, accessible and valuable.
Community
Both in our company and in general, we grow through our ability to cooperate and work as a team. Being adherents of the global open source community, we share our ideas and build upon each other.
Mission
Personality

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow/vision
also: https://realtimeweb.org/hood/introduction/tomorrow/vision
title: Vision · Real Time Web

Vision · Real Time Web
DOCUMENTATION
Vision
Eternal widespread ownership of the Web
At Real Time Web we see the Web (WWW) as the world's biggest marketplace and an unparalleled platform for innovation.
We believe in a web that rewards and protect the interests of the ones who create value. We wish to make sure everyone has the best opportunity to develop their ideas and benefit from what they create.
Our guiding principle is to allow eternal widespread ownership of the Web.
To better solve existing tasks and future development, we wish to fundamentally upgrade the Web, by adding new dimensions.
The Internet of tomorrow
Mission

### PAGE
url: https://realtimeweb.org/docs/introduction/tomorrow
also: https://realtimeweb.org/hood/introduction/tomorrow
title: The Internet of tomorrow · Real Time Web

The Internet of tomorrow · Real Time Web
DOCUMENTATION
The Internet of tomorrow
How the Real Time Web wants to be understood. Not a company brief.
These notes are about direction: who this is for, what it stands for, and how the idea should be told. They are not a private agency document.
Vision
Mission
Values
Personality
Audience
Position
Promise
Proof
Concept
Introduction
When an idea leaves the lab, it needs a clear face. People should know what they are looking at, and what it is not.
Real Time Web is an architecture for a live web. These pages keep the story in one place so the words stay consistent: ownership, live things, and a network that is not captured by one vendor.
The notes are a frame. They can change when the work changes.
How participation works
Vision

### PAGE
url: https://realtimeweb.org/docs/introduction/vision
also: https://realtimeweb.org/hood/introduction/vision
title: Vision and principles · Real Time Web

Vision and principles · Real Time Web
DOCUMENTATION
Vision and principles
Eternal widespread ownership of the Web, and who created the architecture.
Eternal widespread ownership of the Web
We see the Web as the world’s largest marketplace and one of humanity’s most important platforms for communication, creativity, and innovation.
We believe the Web should reward and protect the people and organizations that create its value. Individuals, developers, device owners, service providers, and domain owners should have meaningful control over the resources they contribute to the network, and a fair opportunity to benefit from what they create.
The guiding principle is: Eternal widespread ownership of the Web .
This means building a Web that cannot be permanently captured or controlled by a small number of centralized platforms. Ownership, intelligence, and access control should remain distributed among the participants in the network.
RTW seeks to upgrade the Web by adding new dimensions of live communication, resource ownership, and machine interaction, while preserving the open and decentralized qualities that made the Web successful.
Who created the Real-Time Web?
The Real-Time Web was created by Norwegian technology inventor Paal Kristian Levang.
Its architectural foundation, known as Morphic Architecture Design (MAD), was first introduced by Levang in 2008. The architecture grew out of his work in distributed systems, machine communication, the Internet of Things, semantic technologies, and real-time data exchange.
Over several years, the concepts were developed and tested through research, prototypes, proof-of-concept systems, and commercial technology projects. This work eventually evolved into the Real-Time Web architecture.
RTW is now being introduced as an open technological ecosystem in which developers, organizations, device owners, service providers, and users can create and control their own network resources.
What this site covers
What this site covers. Implementations are independent.
What
Real Time Web
A network architecture for live bidirectional resource relationships
Understand the idea
Why
Ownership of live data
Keep data with its source instead of copying it into platforms
Understand the problem
MAD
Morphic Architecture Design
Four independently owned layers, introduced in 2008
Understand the blueprint
RealTimeWeb.org is a standalone nonprofit site. It is not owned by a company. It tells the reader what the Real Time Web is, why it exists, and introduces MAD.
Next in this path is How participation works , then Morphic Architecture .
How it works
How participation works

### PAGE
url: https://realtimeweb.org/docs/introduction/what-it-can-do
also: https://realtimeweb.org/hood/introduction/what-it-can-do
title: What it can do · Real Time Web

What it can do · Real Time Web
DOCUMENTATION
What it can do
High-level stories of live resources, inherited context, and ownership that can move.
The stories below are teaching cases from the source. They show what live resources can do when they stay with their owners.
The guiding line from the brand work is simple: let anyone connect anything to the present. The present, here, means a live relationship, not a stored page about a thing.
Figure 3-1 concept: Bijective Network System (redrawn from source description)
Connect a thing without rewriting the thing
Take a lamp from a shop. It has a light and a switch. That is its body. You bring it home and look for a service that can turn it on from somewhere else. You register the lamp against that service. The lamp sends and receives through a ghost that stands for that one lamp. The service supplies the intelligence. The lamp supplies the body.
A refrigerator with a camera can do the same job in another context. Register it against a service that watches what leaves the shelf. While you are in a store, that service can tell you the shelf is empty. The fridge did not become a shopping application. It stayed a fridge. The service used a live reading you authorized.
The longer lamp walkthrough, with ghosts, morphing, and ownership, lives in the journal Two webs .
One sensor, many contexts
A temperature sensor only reports a number. That is all its body can do. In a heterogeneous network , that number can be used in more than one place without changing the sensor.
Morph the sensor’s ghost into a light service and the same reading can stand in for a switch: lights on at one threshold, off at another. Morph it into a heat service and it regulates a room. Withdraw the morph and those services lose the reading. The sensor still reads. Ownership of the ghostId did not move.
The object stays itself. The service supplies the context.
The limit is always the body. An object with only a temperature element cannot grow arms. It can inherit context from any Morphic service the owner authorizes. When more services exist, the same modest object can take part in more stories. The collective gets more useful because the parts stay independently owned.
Intelligence arrives at the endpoint
An endpoint does not have to ship with a finished program. In MAD, a connection can be kept alive by something that has almost no logic of its own. The application layer can send a self-contained message first. That step is called kernelizer . The live stream follows after. An empty container can receive its program, then its data, without a preinstalled client.
This is how the architecture talks about “dumb” objects becoming useful on the network. The object is identified. It is paired with a ghost. The service describes itself. Behavior can change while the connection is still open. The owner of the ghost decides which layer may be configured.
A room as a linking path
The partner material uses a living room as a picture, not as a product. A chair, a lamp, a bowl, a radio, and an application can each be a service. The application links to the others. After the links exist, the live values still travel from a specific sensor to a specific application instance owned by the same person.
That is the scale rule. Thousands of chairs can be made. Millions of applications can be open. Data moves for a pair when ownership, or granted read access, matches at both ends. The service providers do not have to run a session table for every pairing. They describe services and links. The linking path does the rest for the people who actually own the ends.
Linking path: data is morphed in local context
Ownership can move with the object
If you leave a home and the washing machine, the lights, and the door stay behind, the interesting question is not how to reinstall each application. It is who owns the ghosts.
A ghost can be transferred. The new holder confirms. After confirm, that person owns the data layer at those endpoints and chooses which services to morph them into. The old holder no longer controls those readings. That is a change of ownership, not a casual share.
Read access is the other action. Morphing a ghost into a secondary service grants a reading that can be withdrawn. The ghostId stays with the owner. Two different people do not open each other’s data because they share an implementation.
Data is consumed when ownership or approved read access is present
Flows
Same owner, two endpoints
You own the lamp ghost. You also own the ghost that represents you inside the scheduler. The ends match. Live data can be consumed.
Or you morph the lamp ghost against the scheduler. That is read access, and you can take it back.
Does not flow
No match, no morph
A neighbor’s lamp is not yours. Sharing an implementation does not open the data. Without ownership or an approved morph, nothing is consumed at the endpoint.
Past, present, and services that do not exist yet
A service can be described before the data for it exists. The source calls this useful when you want to see whether others will link to a product that is not yet shipping. The service waits. When a live source appears, the channel can start.
The same idea works backward. A light application written for one kind of lamp can keep working when a later lamp appears, if the new lamp can be morphed into the same local model. The application does not have to be rewritten for each manufacturer. Each service keeps its own shape. The normalizer fits the incoming source to that shape.
This is the position the brand work aimed for: universal building blocks. Not one vendor’s interface that everyone else must adopt.
Machines use this the way people use the Web
People follow hyperlinks through information. Machines need a place to exchange live values, change context at runtime, and keep ownership answerable. The source describes RTW as that place: an Internet of Everything network that can sit next to the World Wide Web.
AI agents in the source are participants, not the product. A service can have one or several agents. They work on the live channel the owner authorized. The network does not become a single mind owned by one company. It grows as independent domains and services are added.
Keep reading
Next in this path is How it works . The pairing and the services come after that, under Morphic Architecture.
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Data and information
How it works

### PAGE
url: https://realtimeweb.org/docs/introduction/why
also: https://realtimeweb.org/hood/introduction/why
title: Why Real Time Web? · Real Time Web

Why Real Time Web? · Real Time Web
DOCUMENTATION
Why Real Time Web?
Limitations of today’s Web architecture and why a shared model for live resources is needed.
The Internet and the World Wide Web were not originally designed for a world containing billions of continuously changing sensors, actuators, autonomous machines, AI agents, and user-controlled data sources.
Limitations of today’s Web
The World Wide Web is highly effective for publishing and retrieving information, but several limitations become apparent when it is applied to live machines and resources:
Hyperlinks are primarily one-way relationships.
Live bidirectional communication requires additional technologies.
Sessions, identity, authentication, and trust are repeatedly implemented by individual services.
Resource ownership and access control are often delegated to centralized platforms.
Data is frequently copied from its source and stored by intermediaries.
APIs are commonly designed for a particular provider, application, or data model.
Integrating heterogeneous systems requires extensive middleware and custom development.
APIs have made machine-to-machine communication possible across many different systems. However, an API normally exposes a predefined interface controlled by a particular service provider. Consumers must adapt to that interface, authenticate with that provider, and rely on the provider’s infrastructure and data model.
As the number of connected resources grows, this approach can produce a fragmented landscape of APIs, databases, authentication systems, cloud platforms, and proprietary integrations.
What fragmentation looks like
Today, these resources are commonly connected through cloud platforms, APIs, middleware, and centralized databases. The result is an environment in which:
Live data is repeatedly copied and stored in different systems.
Applications depend on provider-specific APIs.
The same integrations must be developed many times.
Users often surrender control over their data to centralized platforms.
Devices and services cannot easily understand or communicate with one another.
Identity, authentication, payments, and trust are implemented separately for each service.
AI agents and autonomous machines lack a common environment for discovering and interacting with live resources.
A shared architecture
RTW addresses these challenges by providing a shared architecture for directly addressable, bidirectionally connected resources. Its purpose is to make live resources easier to discover, authorize, combine, transform, and use across organizational and technological boundaries.
A heterogeneous network is not controlled by a single entity. It evolves continuously as independent participants connect and manage their own domains and services. Each participant contributes to a collective, self-growing ecosystem while retaining control over its own resources.
This gives creators and developers the freedom to build new services without requiring the entire network to adopt one vendor, one data model, or one centralized platform.
Does RTW replace the Internet?
No. RTW is designed to operate on top of and alongside the existing Internet.
The Internet provides the underlying global infrastructure for transporting data. The World Wide Web provides an established system for publishing, linking, and retrieving information. RTW uses this existing foundation while adding mechanisms for live, bidirectional relationships between physical and virtual resources.
A conventional website can continue to deliver documents, images, and videos, while RTW can provide live data channels and interactions behind or alongside that website.
The longer why sits next to this page: The Internet of tomorrow . Next in this path is Data and information . The lamp story is in the journal Two webs .
Under the hood
Want to see how live channels work? Read the blueprint →
What is Real Time Web?
Concept

### PAGE
url: https://realtimeweb.org/docs/introduction
also: https://realtimeweb.org/hood/introduction
title: What is the Real-Time Web? · Real Time Web

What is the Real-Time Web? · Real Time Web
DOCUMENTATION
What is the Real-Time Web?
A framework and network architecture for connecting live physical and virtual resources across the Internet.
RealTimeWeb.org is a standalone nonprofit site. It explains what the Real Time Web is, why it exists, and introduces Morphic Architecture Design (MAD).
The site is independent. The idea can be built by more than one party.
The Real-Time Web (RTW) introduces a new architecture for connecting, transforming, and exchanging live data across the Internet. It is designed to enable machine automation and addressing the Internet of Everything , including physical devices, virtual resources, software services, AI agents, sensors, actuators, and people, so they can participate in the same connected ecosystem.
The original World Wide Web was primarily designed for publishing and sharing information such as text, images, documents, and video. The Semantic Web later extended this model by making information more structured and machine-readable.
The Real-Time Web takes the next step. It introduces a live, bidirectional linking model that allows network resources to be connected directly to one another. Instead of treating data as static content retrieved from a website, RTW treats live data sources and network resources as addressable participants in the Web.
This makes it possible to connect almost any physical or virtual resource to live services through a heterogeneous and user-controlled network architecture.
Figure 3-1 concept: Bijective Network System (redrawn from source description)
From hyperlinks to live relationships
A conventional hyperlink points from one resource to another. The relationship is normally one-way: the source knows where the link points, but the target does not necessarily know which resources link to it.
RTW extends this concept by introducing a bidirectional and bijective relationship between network resources. In this model, each participating endpoint has a unique corresponding representation in the network. The relationship can therefore be addressed and maintained from both sides.
This enables data to flow directly from its live source to an authorized receiving service, application, device, or user instance.
World Wide Web
Real-Time Web
Read the next pages in order: Why Real Time Web? , then Data and information . The lamp walkthrough now lives as a journal: Two webs .
Rather than copying all data into a centrally controlled platform, RTW is designed to keep data associated with the resource and domain where it was generated. The owner can determine whether the resource is available, who may access it, and under which conditions it may be used.
Applications may process, transform, and combine authorized data into new contexts and services. The application provider controls the transformation logic, while the data owner retains control over access to the original source. This separation supports innovation without requiring the creator of a service to take ownership of the underlying data.
What RTW provides
RTW therefore provides a foundation for:
Live and bidirectional data exchange
Directly addressable physical and virtual resources
Distributed machine intelligence
User-controlled access to data
Interoperability across different systems and resource types
Reduced dependence on centralized data platforms
Product, protocol, or architecture?
RTW is primarily a network architecture and technological framework. It is not a single application or standalone product.
This site covers what RTW is, why it exists, and Morphic Architecture Design:
What this site covers. Implementations are independent.
What
Real Time Web
A network architecture for live bidirectional resource relationships
Understand the idea
Why
Ownership of live data
Keep data with its source instead of copying it into platforms
Understand the problem
MAD
Morphic Architecture Design
Four independently owned layers, introduced in 2008
Understand the blueprint
This is comparable to the distinction between the World Wide Web as a general architecture and the browsers, servers, standards, and services built around it.
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Why Real Time Web?

### PAGE
url: https://realtimeweb.org/docs/reference/contributing
also: https://realtimeweb.org/hood/reference/contributing
title: Contributing · Real Time Web

Contributing · Real Time Web
DOCUMENTATION
Contributing
How to offer writing for this site, how credit works, and what is refused.
This site is for the people who want to understand the Real Time Web. It is written for people, by people. It is not a shop window.
If you want to write here, send the work. It will be read. If it is published, you will be named as the author.
How to send writing
Send the draft to both addresses. Articles, field notes, and documentation copy all go the same way.
thiru@synx.tools
paal@synx.tools
We review what you send. Review is editorial. It is not a product intake, and it is not a lead form.
What this site will publish
Work that explains the architecture, the ownership model, or a live demonstration of the idea.
The same rules as the rest of the site apply:
Conceptual questions live here.
No account is created here.
Anyone can develop an implementation of MAD or RTW. This page does not pick one.
What this site will not publish
There are no ads on RealTimeWeb.org. There is no business promotion. There is no tool promotion. There is no join button, no pricing, and no outbound product pitch.
A contribution that asks to promote a company, a product, a toolchain, a marketplace, or a paid placement will be refused in full. That request is blocked. The sender will not be invited to contribute again.
This is not a warning for tone. It is the condition of writing here. The Real Time Web, on this site, stays a public explainer. It does not become a catalogue.
Credit
If the writing is accepted, your name appears as the author. That is the credit. There is no sponsored byline, and there is no paid mention in the body.
If you want the layers first, read Morphic Architecture . If you want who controls what, read Governance .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Experiments
Governance

### PAGE
url: https://realtimeweb.org/docs/reference/faq
also: https://realtimeweb.org/hood/reference/faq
title: FAQ · Real Time Web

FAQ · Real Time Web
DOCUMENTATION
FAQ
Answered questions from the RealTimeWeb.org source, plus pending items.
RealTimeWeb.org is a standalone nonprofit site. It explains what the Real Time Web is, why it exists, and introduces Morphic Architecture Design (MAD).
The site is independent. The idea can be built by more than one party.
Every FAQ answer is structured as a direct first sentence, a short explanation, and a link to a guide.
General understanding
What is the Real-Time Web?
The Real-Time Web (RTW) is a framework and network architecture for connecting live physical and virtual resources across the Internet.
It allows sensors, actuators, devices, applications, AI agents, services, data sources, and people to participate in the same distributed network. Instead of relying entirely on centralized platforms, copied datasets, and provider-specific APIs, RTW creates direct, bidirectional relationships between authorized network resources.
RTW is designed to give each participating endpoint a persistent network identity while allowing data, access rules, and transformation logic to change dynamically.
In simple terms, the World Wide Web connects documents and information. The Real-Time Web extends this model to connect live data, machines, services, and physical objects.
Introduction
Is RTW a product, protocol, or network architecture?
RTW is primarily a network architecture and technological framework.
It defines principles and mechanisms for identifying resources, creating bidirectional relationships, exchanging live data, managing access, and coordinating different ownership layers. It is not a single application or standalone product.
Vision
Why is a new network architecture needed?
The Internet and the World Wide Web were not originally designed for billions of continuously changing sensors, actuators, autonomous machines, AI agents, and user-controlled data sources.
These resources are commonly connected through cloud platforms, APIs, middleware, and centralized databases, each with its own interfaces and identity systems.
Why Real Time Web?
How is RTW different from the World Wide Web?
The World Wide Web is primarily designed around documents and resources that are identified by URLs and retrieved using requests. A hyperlink generally points in one direction.
The Real-Time Web extends this model from static or request-based resources to live, stateful network relationships.
World Wide Web
Real-Time Web
Two webs
What does bijective network architecture mean?
It means each participating endpoint has one corresponding ghost, and that ghost represents that one endpoint. The relationship is uniquely addressable from both sides.
A conventional hyperlink points one way. The bijective pairing is live and bidirectional. If a ghost could stand for two endpoints at once, ownership of the data would stop being answerable.
Bijective network
What is a real-time data channel?
A data channel is how a linking path collects live sources into a channel of data associated with one user’s ghost in a local service.
The canonical picture is temperature from several makers, gathered for one person. Only data with a valid morphed ghost is received. Both ends need a user who owns the data or has been granted read access.
Data channels
How is data exchanged between network participants?
Authorized updates can travel along a linking path as they occur. Each service morphs the value into its own local model. The network does not natively store the value.
Data is consumed at an endpoint when the ghosts at the ends are owned by the same user, or the receiver has approved read access. Two different people do not open each other’s data because they share an implementation.
Morphic services
Does RTW require centralized servers or cloud services?
No centralized API or database is required to build RTW services in this model.
Each service works on local structures. A service may attach a database to its local ghosts after it has received a morph. That local copy is optional. The architecture is designed to sit on the existing Internet and to grow as independent domains and services are added.
Why Real Time Web?
Is RTW intended to replace the existing Internet?
No. RTW is designed to operate on top of and alongside the existing Internet.
The Internet transports data. The World Wide Web publishes and retrieves information. RTW adds live, bidirectional relationships between physical and virtual resources.
Who created the Real-Time Web?
The Real-Time Web was created by Norwegian technology inventor Paal Kristian Levang. Morphic Architecture Design was first introduced in 2008.
Vision and principles
Can anyone implement MAD or RTW?
Yes. MAD and the Real Time Web can have more than one builder.
RealTimeWeb.org is a standalone nonprofit site. It publishes the architecture.
Reference implementations
Can other companies build compatible RTW implementations?
Yes. RTW is the architecture. Compatible protocols, tools, services, and commercial products can be built on it. The architecture is shared. The builders can be different.
How it works
Is there a reference implementation?
The source names one known pair: a marketplace for domains and participation, and a toolchain used to configure and maintain services.
Those names sit beside How it works . Other parties may implement MAD.
Synx
Architecture
How does the RTW network topology work?
MAD constructs data channels from sources that have been morphed along a linking path. Each service only sees local context. How a value was morphed is unknown outside that service.
There is no centralized API or database required to build RTW services. Data is consumed when the ghosts at the ends are owned by the same user, or the receiver has approved read access. This answer follows draft architecture notes.
Network topology
How are services, devices and AI agents identified?
They are identified as endpoints with one corresponding ghost. The pairing is bijective and addressable from both sides.
A Morphic service is itself a ghost in the application layer. Ghost id zero is the service. How identifiers are written on the wire is not specified in the current source.
Identity
What is an RTW domain?
A domain is an address space you control. It is not a website URL.
If you own the whole stack of a domain, you also control ownership of allocated ghosts for endpoints connecting against that address space. How a public name is registered remains unanswered.
Domains
How does RTW reduce unnecessary network traffic?
If nobody is listening, the value does not need to travel. Data stays associated with the resource where it was generated, rather than being copied into a central store that answers whether or not the reading changed.
That is the architectural claim in the draft notes. It is not a congestion-control specification.
Network topology
What is Ghost Space?
Ghost Space is the shared coordination environment around a network resource. A ghost is a shared-memory representation of one endpoint.
The four layers can observe authorized updates without one party owning the whole stack. Ghost Space is not a chat room. The ghost is tied to a resource, not to a person.
Ghost Space
What is a Morphic service?
A Morphic service is an application-layer service on MAD that allocates ghosts for users.
When the service is created, the service owner is primary owner of those ghosts. After a user confirms a transfer, the user owns the data layer. The service owner keeps the application layer and may keep a local copy.
Morphic services
What is the difference between morph and transfer?
Transfer moves ownership of the ghostId after the user confirms. Morph grants read access into another service and can be withdrawn.
Two different people do not open each other’s data because they share an implementation. One of them morphs or transfers.
Morphic services
What is a micropage?
A micropage is a mini description a service owner publishes of the service and its data model.
RTW is protocol independent. The service owner chooses the protocol. If a service does not describe itself, other services have no serious basis for linking to it.
Morphic services
What is a kernelizer?
A kernelizer lets an endpoint receive a self-contained message before the data stream. An empty endpoint can get a program first, then data, without a preinstalled application.
Ownership of the ghost decides which layer can be configured at runtime. This answer follows draft architecture notes.
Interoperability
Is RTW protocol independent?
Yes. The service owner decides their own protocol. How data is structured is described on the micropage.
This site does not publish encodings, command tables, or a required schema language.
Interoperability
Trust, control and security
Who owns data exchanged through RTW?
The data source is owned by the user that controls the endpoint and has registered it against the endpoint ghost. The ghost can be transferred to another person. Morphing the ghost against a secondary service gives read access that the owner can withdraw.
When a Morphic service is created, the service owner is primary owner of allocated ghosts. After registration and confirmation, the data layer belongs to the user; the application layer remains with the service owner.
Resource / Ownership Layer
Where is data stored?
Data is not natively stored in the network. Data is dynamically morphed into local data models along the linking path. A service owner may persist data in the local context they receive. The network natively does not store data, but a service provider may connect a database to local ghosts.
How is access authorized?
Authentication is optional in MAD. An implementation may use any token system that generates a token for identity.
Once a user is registered in an implementation, they may participate in RTW and become members of services by getting access to ghosts.
Authentication
How can access be revoked?
Morphing a ghost against a secondary service grants read access that the owner can withdraw at any time. A ghost can also be transferred, which is a change of ownership.
Implementations may additionally revoke tokens. Those operational details belong with each implementation, not on this architecture site.
Resource / Ownership Layer
How does RTW protect identities and network resources?
A ghost is a proxy for the network resource, operating in multiple layers, bijectively connected to the endpoint. It provides identity, behavior, and context when an active connection is present.
Ghost Space
How does RTW support GDPR and data sovereignty?
The user needs to control who has access to the data source, and data is not persisted in the network space unless the user has agreed to it. Ownership of a ghost and a direct path to the original source lets the user morph the ghost into a secondary service and share data with them.
How can researchers and developers contribute?
Send writing to both review addresses. If it is published, you are credited as the author.
Promotional requests are refused. Ads, business pitches, and tool pitches are blocked, and the sender is not invited again. A formal specification process remains unanswered.
Contributing
Pending questions
These are listed in the source FAQ plan and do not yet have answers.
Standards and implementation, unanswered:
Is RTW an open specification?
Which specifications are currently available?
How are specifications versioned?
Where can I find technical documentation?
Dictionary
Technical Resources

### PAGE
url: https://realtimeweb.org/docs/reference/governance
also: https://realtimeweb.org/hood/reference/governance
title: Governance · Real Time Web

Governance · Real Time Web
DOCUMENTATION
Governance
Who controls what on the Real Time Web, and what this site is allowed to decide.
Architecture proposal
The source lists a governance and contribution section. It does not provide a process, a board, or a versioned specification. This page states only what is already written: how ownership is split, and what this nonprofit site is for.
Governance, on the Real Time Web, is not a company login. It is the question of who may change a layer without taking the rest.
This site answers that question at the architectural level. It does not run the network.
What this site covers. Implementations are independent.
What
Real Time Web
A network architecture for live bidirectional resource relationships
Understand the idea
Why
Ownership of live data
Keep data with its source instead of copying it into platforms
Understand the problem
MAD
Morphic Architecture Design
Four independently owned layers, introduced in 2008
Understand the blueprint
Two different jobs
Keep these separate. They are easy to mix up.
This site is a standalone nonprofit explainer. It is not owned by a company. It publishes what the Real Time Web is, why it exists, and Morphic Architecture Design.
An implementation is software someone builds on that architecture. Tools, marketplaces, and services sit there. They are not this site.
Conceptual questions live here. Account, marketplace, and onboarding questions live with whichever implementation a person chooses. Configuration and operations live with that implementation’s own documentation.
Who controls which layer
MAD was introduced in 2008 by Paal Kristian Levang. It splits the stack so a change in one layer does not have to redefine the whole relationship.
Four layers. Four possible owners.
Layer Who What it does Teaching picture
L1 Infrastructure Hosting, hardware, connectivity Processing, links, energy, storage where required The roads
L2 Network and security Whoever runs addressing and trust Identity, authentication, authorization, secure communication The checkpoint
L3 Domain and application Service developer Services, linking, transformation logic The shop
L4 Resource and ownership The person, machine, or device that owns the resource Whether the data may be accessed or shared The goods, and who may use them
L1 · Infrastructure
Hosting, hardware, connectivity
Processing, links, energy, storage where required
The roads
L2 · Network and security
Whoever runs addressing and trust
Identity, authentication, authorization, secure communication
The checkpoint
L3 · Domain and application
Service developer
Services, linking, transformation logic
The shop
L4 · Resource and ownership
The person, machine, or device that owns the resource
Whether the data may be accessed or shared
The goods, and who may use them
Infrastructure providers control processing, connectivity, and energy.
Network and security providers manage addressing, identity, and trust. Authentication is optional in the model.
Service developers own their applications and transformation logic.
Resource owners control whether a source may be accessed or shared.
The hardware provider, the network operator, the application developer, and the end user do not have to be the same party. That is the design. A heterogeneous network is not controlled by a single entity. It grows as independent participants add their own domains and services.
Who owns the data
Ownership of data at an endpoint is given by the ghostId. Whoever owns the ghostId owns the data at that endpoint.
When a Morphic service is created, the service owner is the primary owner of allocated ghosts. After a user registers and confirms a transfer, the data layer belongs to the user. The application layer stays with the service owner. The service owner may keep a local copy.
Two different people do not open each other’s data because they share an implementation. Read access is a morph. It can be withdrawn. Ownership is a transfer, and a transfer has to be confirmed.
The network does not natively store data. A service may attach a database to its local ghosts. That local copy is the service’s context. It is not a required central store.
Data is consumed when ownership or approved read access is present
Flows
Same owner, two endpoints
You own the lamp ghost. You also own the ghost that represents you inside the scheduler. The ends match. Live data can be consumed.
Or you morph the lamp ghost against the scheduler. That is read access, and you can take it back.
Does not flow
No match, no morph
A neighbor’s lamp is not yours. Sharing an implementation does not open the data. Without ownership or an approved morph, nothing is consumed at the endpoint.
Eternal widespread ownership
The guiding principle is eternal widespread ownership of the Web.
That means the Web should not be permanently captured by a small number of platforms. Ownership, intelligence, and access control should remain distributed among the people and organizations that contribute resources.
This site exists so that sentence has a public home. It is not a marketplace. It is the architecture those marketplaces would have to remain compatible with.
What is not decided here
These questions appear in the source plan. They do not yet have answers.
Is RTW an open specification?
Which specifications are currently available?
How are specifications versioned?
Where is the technical documentation for an implementation?
Writing for this site has a review path. That is editorial, not a standards process. See Contributing .
Until those are written, this site will not invent a standards body, a voting process, or a contribution workflow. Publishing the architecture is not the same as running a specification program.
If you want the layers, read Morphic Architecture . If you want how live channels work, read How it works . If you want the terms, read Dictionary .
MAD
Want an introduction to Morphic Architecture Design? Read Morphic Architecture →
Contributing
Proof

### PAGE
url: https://realtimeweb.org/docs/research/experiments
also: https://realtimeweb.org/hood/research/experiments
title: Experiments · Real Time Web

Experiments · Real Time Web
DOCUMENTATION
Specification under development
Listed as a planned section. Body copy has not been provided yet.
Experiments
A slot for proofs and tests. No experiment writeups were supplied in the source.
This section is listed in the RealTimeWeb.org plan. The current source does not include approved experiment writeups.
A valid proof in this architecture is one live service: a source, an owner, a channel, and a visible effect. Until those notes are written, this page stays a slot.
See Reference implementations for named implementations at high level.
Reference Implementations
Contributing

### PAGE
url: https://realtimeweb.org/docs/research/implementations
also: https://realtimeweb.org/hood/research/implementations
title: Reference Implementations · Real Time Web

Reference Implementations · Real Time Web
DOCUMENTATION
Reference Implementations
Named implementations are listed beside How it works : Synx, Morph Space, and Skalle.
MAD and the Real Time Web can have more than one builder.
Skalle
Experiments

### PAGE
url: https://realtimeweb.org/docs/research
also: https://realtimeweb.org/hood/research
title: Technical Resources · Real Time Web

Technical Resources · Real Time Web
DOCUMENTATION
Specification under development
Listed as a planned section. Body copy has not been provided yet.
Technical Resources
Research papers and technical resources. No bibliography was provided in the source.
This section is listed in the RealTimeWeb.org plan as research papers and technical resources.
No paper list, DOI list, or approved bibliography appears in the current source. This page will not invent citations.
What belongs here later
Research papers that introduce or test MAD and the Real Time Web
Technical resources that stay at the architecture level
Links to experiments once those notes are written
Pointers to reference implementations
What is already named
Named implementations sit beside How it works .
Until a bibliography is supplied, treat this page as a slot, not as a library.
FAQ
Synx

### PAGE
url: https://realtimeweb.org/docs/specification/versions
also: https://realtimeweb.org/hood/specification/versions
title: Version History · Real Time Web

Version History · Real Time Web
DOCUMENTATION
Specification under development
Listed as a planned section. Body copy has not been provided yet.
Version History
The source lists “Specifications and version history” as a planned section without body copy.
MAD was first introduced in 2008. How specifications will be versioned is an unanswered FAQ item.
Proof
Summary

### PAGE
url: https://realtimeweb.org/docs/summary
also: https://realtimeweb.org/hood/summary
title: Summary · Real Time Web

Summary · Real Time Web
DOCUMENTATION
Summary
What the About RTW path has covered so far.
The Real Time Web is a network architecture for connecting live physical and virtual resources with bidirectional relationships. It is not a single app, not a replacement for the Internet, and not the World Wide Web.
Morphic Architecture Design is the blueprint behind it, introduced in 2008 by Paal Kristian Levang. Four layers can have different owners: infrastructure, network and security, domain and application, and resource and ownership. A change in one layer does not have to redefine the whole relationship.
Each network resource is an endpoint. Each endpoint has one ghost. Ghost Space is the shared state around that resource so the four layers can observe authorized updates without one party owning the whole stack.
A transfer moves ownership of a ghostId after the user confirms. A morph grants read access that can be withdrawn.
Keyword terms sit in the Dictionary . Draft topics sit under Still open, after that dictionary.
Version History

### PAGE
url: https://realtimeweb.org/docs
title: Introduction to the Real-Time Web · Real Time Web

Introduction to the Real-Time Web · Real Time Web
ABOUT RTW
Introduction to the Real-Time Web
A Real-Time Web framework for Internet of Everything systems.
The Real-Time Web (RTW) is a new architecture for connecting, transforming, and exchanging live data across the Internet. It is written for a world in which machines, services, and people need to work with one another in the present, not only through pages that were stored yesterday.
It is designed to support machine automation and to address the Internet of Everything : physical devices, virtual resources, software services, AI agents, sensors, actuators, and people, so they can take part in the same connected ecosystem.
The original World Wide Web was built to publish and share information: text, images, documents, and video. The Semantic Web later extended that model by making information more structured and easier for machines to read.
The Real-Time Web takes the next step. It introduces a live, bidirectional linking model that lets network resources connect directly to one another. Instead of treating data as static content retrieved from a website, RTW treats live data sources and network resources as addressable participants on the Web.
This makes it possible to connect almost any physical or virtual resource to live services through a heterogeneous , user-controlled network architecture.
The chapters below are meant to be read in order. Each one assumes the one above it.
Start here. What it is, why a new architecture is needed, how it differs from the World Wide Web, what live data is, and what that makes possible.
How it works. Live channels, the guiding principle, and how participation is structured.
The architecture. Morphic Architecture Design, the four layers, ghosts, the bijective pairing, Morphic services, data channels, and network topology.
Summary. What that path has covered so far.
Under the hood opens Blueprint . The Dictionary and Still open follow there.
What this site covers. Implementations are independent.
What
Real Time Web
A network architecture for live bidirectional resource relationships
Understand the idea
Why
Ownership of live data
Keep data with its source instead of copying it into platforms
Understand the problem
MAD
Morphic Architecture Design
Four independently owned layers, introduced in 2008
Understand the blueprint
RealTimeWeb.org is a standalone nonprofit site. It explains what the Real Time Web is, why it exists, and introduces Morphic Architecture Design (MAD).
The site is independent. The idea can be built by more than one party.
Common questions
These are the questions the source puts on RealTimeWeb.org first. Short answers live on FAQ . Each one points to the page that owns the topic.
What is the Real-Time Web?
Is RTW a product, protocol, or network architecture?
Why is a new network architecture needed?
How is RTW different from the World Wide Web?
Is RTW intended to replace the existing Internet?
Who created the Real-Time Web?
Who owns data exchanged through RTW?
Where is data stored?
How is access authorized?
Can anyone implement MAD or RTW?
What is Real Time Web?

### PAGE
url: https://realtimeweb.org/hood/implementation/morph
title: Morph Space · Real Time Web

Morph Space
High-level note on Morph Space as a known MAD implementation.
Real Time Web is the network concept and architecture. Morph Space is a commercial platform and a known implementation. This page names that role.
Morph Space is named in the source as a marketplace and environment. Through it, people and organizations can establish domains, publish resources, and participate in a live network built on MAD.
The current known implementation of MAD is Morph Space. That network uses Synx tools for configuration and operations.
A domain here is an address space, not a marketing website. How names are registered, how long setup takes, and what the screens look like are not specified as public copy on this site.
Account and marketplace questions belong with Morph Space. The architecture questions belong here.
See also Synx and How it works .
Synx
Skalle

### PAGE
url: https://realtimeweb.org/hood/specification/communication
title: Communication Specification · Real Time Web

Specification under development
Listed as a planned section. Body copy has not been provided yet.
Communication Specification
Protocol independence and service description. Wire formats are not specified here.
This section is listed in the source as specifications and version history. Written protocol text has not been supplied.
What the architecture says
RTW is protocol independent. The service owner decides their own protocol.
Information about how data is structured lives on each micropage: a mini description of the service and its data model. Any service that wants to be linked should describe its schema. If that description is missing, other services have no serious basis for linking to it.
An implementation may use common Internet transports and more than one encoding. Format details, command tables, and default encodings belong with that implementation.
What is not written
A required schema language
A versioned protocol document
A discovery or name-resolution specification
See Interoperability for normalizer, materializer, and kernelizer, and Morphic services for the micropage.
Specification under development
Listed as a planned section. Body copy has not been provided yet.
Protocol Overview
Network

### PAGE
url: https://realtimeweb.org/hood/specification/data-channels
title: Data Channels Specification · Real Time Web

Specification under development
Listed as a planned section. Body copy has not been provided yet.
Data Channels Specification
Planned section. See the architecture proposal for Data Channels . A formal channel protocol is not in the source.
Security
Dictionary

### PAGE
url: https://realtimeweb.org/hood/specification/identity
title: Identity Specification · Real Time Web

Specification under development
Listed as a planned section. Body copy has not been provided yet.
Identity Specification
Planned section. No identity specification text is provided.
Conceptual material lives under Identity and Authentication . Cryptographic mechanisms are intentionally unspecified here.
Network
Security

### PAGE
url: https://realtimeweb.org/hood/specification/network
title: Network Specification · Real Time Web

Specification under development
Listed as a planned section. Body copy has not been provided yet.
Network Specification
Planned section. The source does not include a versioned network specification.
Draft architecture notes mention a horizontal linking path without a centralized API or database. Those notes still need team approval and are not a specification.
Related conceptual pages: Morphic Architecture , Discovery .
Communication
Identity specification

### PAGE
url: https://realtimeweb.org/hood/specification/security
title: Security Specification · Real Time Web

Specification under development
Listed as a planned section. Body copy has not been provided yet.
Security Specification
Planned section.
The source states that the MAD network does not natively persist data into databases or filesystems, is tokenized, and can use any token system that generates a token for identity. Access can be revoked. Morphing a ghost against a secondary service grants read access that the owner can withdraw.
A complete security specification is not provided.
Related: Network / Security Layer , Authentication .
Identity specification
Data channels specification

### PAGE
url: https://realtimeweb.org/hood/specification
title: Protocol Overview · Real Time Web

Specification under development
Listed as a planned section. Body copy has not been provided yet.
Protocol Overview
Planned specification section. No body copy is provided in the source yet.
This section is listed in the source as a recommended RealTimeWeb.org area: specifications and version history. Written protocol text has not been supplied.
RTW is primarily a network architecture and technological framework. Compatible protocols, tools, services, and products can be built on it. Anyone can develop an implementation of MAD or RTW. RTW is protocol independent: the service owner decides their own protocol in the current architectural notes.
Specification under development
Listed as a planned section. Body copy has not been provided yet.
Blueprint
Communication

### PAGE
url: https://realtimeweb.org/
title: Real Time Web

Real Time Web
Skip to content REAL TIME WEB About RTW Journals Under the hood Contact
THE REAL TIME WEB
The network worth
owning .
A live web for people, devices, services, and ideas, where what you create stays yours, and the network keeps growing around it.
Explore Real Time Web

### PAGE
url: https://skalle.ai/architecture
title: Architecture — Skalle AI

Architecture — Skalle AI
/05 Architecture
Architecture
The Real Time Web defines the network. Morph Space is how people and organizations join it. Synx tools are the controls used to configure, secure, and operate it afterward.
01 Intent Ordinary language
02 Skalle Creates and links
03 Synx tools Name, operate, access
04 Morph Space Where it is joined
05 Real Time Web Where it runs
06 Owned service Stays with the owner
Through MCP, your model is the intelligence and Skalle is the Real Time Web capabilities. Skalle is not tied to one model. No single AI model has to own the ecosystem. No single cloud has to own the infrastructure. You remain in control of your services and data.
A live web for people, devices, services, and ideas, where what you create stays yours, and the network keeps growing around it.
The abstraction is the network, not a folder of files or a list of APIs. Applications are composed from independently owned resources: data, intelligence, machines, and services.
/06 Layers
A service sits on a stack. Skalle does not replace the stack. It helps you name the layer you are changing.
01
Infrastructure
Machines, connectivity, and energy.
02
Network and security
Addressing, identity, and trust.
03
Domain and application
Services, links, and transformation.
04
Resource and owner
What is owned, and who it belongs to.
A field you join, not a platform you rent
The Real Time Web is a live field for people, machines, services, and ideas. What you make can stay with you while the field keeps growing around it. Morph Space is how people and organizations join. Synx tools are the controls used afterward to name, operate, and secure a domain. Skalle is the interface that speaks those controls.
01 Ref ES_ 01
Words 58
Read 1 min
Links instead of a private door
Machines need the change, not another page. A service can use another service by a link. The stream does not have to be copied into a warehouse in the middle. When a device changes hands, the right to use what it carries can move with the owner.
02 Ref ES_ 02
Words 47
Read 1 min
Trade is still ahead
Synx Trade is planned as a marketplace for this kind of service. It is not a live product on this site. What is live in the story is the path you can already describe: a service, a Ghost, a link, and an owner.
03 Ref ES_ 03
Words 43
Read 1 min
/07 Representation
A map of the system as it is described publicly. Nothing on this panel is read from a live backend.
Skalle Interface
Synx DNS Naming
Synx BIOS Operating
Synx Pass Identity
Real Time Web Network

### PAGE
url: https://skalle.ai/lab
title: Lab — Skalle AI

Lab — Skalle AI
/04 Lab
Lab
The controls around Skalle. Each panel is a role in the toolchain, not a live status feed.
LAB_001 NAMING
Synx DNS
Decentralized domain registration and mapping for the Real Time Web. A Real-Time Domain is how an autonomous endpoint gets a readable name, in public or in private business networks. It is the onboarding gateway.
Open ↗ LAB_002 OPERATING
Synx BIOS
The decentralized operating layer. It administers services across the stack, shares or transfers a data source, and shows what you own. It is network-agnostic and event-driven. The network does not store the stream.
Open ↗ LAB_003 IDENTITY
Synx Pass
Identity and access for a decentralized network. Synx Pass recognizes people, services, and machines. When ownership moves, access moves with it.
Open ↗ LAB_004 ENTRY
Morph Space
Where people, AI agents, and machines enter the Real Time Web together. Register a domain, use the Synx tools, and publish Morphic Services other applications can depend on.
Open ↗
Synx names it, operates it, and secures who it belongs to. Skalle AI helps create, link, and administer it.
/05 With Skalle
Each control stays itself. Skalle is the conversation that calls it, inside the identity you already have.
01
Naming
When you ask Skalle to put a service on your domain, the name it receives is a Real-Time Domain. Skalle does not invent a second addressing scheme. It uses the naming layer Synx DNS already is.
02
Operating
Sharing a source, seeing what you own, and moving a stream without parking it in the middle belongs to Synx BIOS. Skalle calls that layer. It does not become the operating system.
03
Identity
People, services, and machines are recognized in Synx Pass. When you tell Skalle to grant access, or to move a Ghost to a new owner, the right follows that identity.
04
Entry
Morph Space is where the service is joined to the network. Skalle can sit there as the conversation: create a Morphic Service, find what is already published, and administer what you own.
/06 Who it is for
The same network, three seats. Skalle is how you speak to the seat you hold.
01
Developers
Build a service and link it, instead of standing up a private API for every neighbor.
02
Domain owners
Hold the namespace and the logic. They do not hold the consumer’s data.
03
Consumers
Sit at the data layer. When a device changes hands, the resource can transfer with it.

### PAGE
url: https://skalle.ai/research
title: Research — Skalle AI

Research — Skalle AI
/03 Research
Research
What is written about Skalle on synx.tools. These are documented positions, not instrument readings.
EXP_001
Natural language
You do not hand Skalle a configuration file. You describe the service the way you would describe it to a colleague. Skalle turns that description into operations the Real Time Web can run.
DOCUMENTED 2026 Read ↗
EXP_002
Autonomous service
One request can become a sequence: create the service, attach a source, link a neighbor, and set who may use the result. Skalle only takes the steps your identity already allows. Asking does not grant a new right.
DOCUMENTED 2026 Read ↗
EXP_003
Model boundary
MCP is how a model you already trust calls the operations Skalle exposes. The model reasons. Skalle does not replace it, and it is not locked to one vendor. Synx holds the network controls underneath.
DOCUMENTED 2026 Read ↗
EXP_004
Network abstraction
The unit of work is not a folder of files. It is a service, a source, a machine, or a right, owned by someone and linked to the next thing. Skalle is taught that shape, so the conversation is about the network.
DOCUMENTED 2026 Read ↗
EXP_005
Owned presence
A Ghost is a device or a source other services can attach to, without lifting the data out of the owner’s hands. A Morphic Service is what those neighbors depend on. The maker keeps the ownership.
DOCUMENTED 2026 Read ↗
EXP_006
Separate from the nonprofit
realtimeweb.org explains the network and Morphic Architecture Design. It is a standalone nonprofit site. Skalle is not that nonprofit. Synx makes the tools. The network is not a company.
DOCUMENTED 2026 Read ↗
From a sentence to a service
The long aim is simple to say and strict to keep. You describe what should exist. Skalle works with the Synx tools and the Real Time Web to decide which resources to connect, then carries the authorized steps. No single model has to own the ecosystem. No single cloud has to own the infrastructure. You remain in control of your services and your data.
01 Ref ES_ 01
Words 64
Read 1 min
Inside Morph Space
Skalle is meant to sit inside Morph Space as the conversation for that ecosystem. From there it can help create Morphic Services, connect sources inside and outside the domain, discover what is already published, propose how things should link, set ownership and access, compose data and intelligence into a new service, and administer the resources you already hold.
02 Ref ES_ 02
Words 58
Read 1 min

### PAGE
url: https://skalle.ai/system
title: System — Skalle AI

System — Skalle AI
/02 System
System
Skalle takes a sentence through the Synx toolchain and leaves a service on the network. It is not a coding assistant.
01
Describe
Say what should exist, in ordinary language.
02
Discover
Find services and sources already on the network.
03
Create
Make the service that should do the work.
04
Link
Connect resources. A neighbor does not require a new private API.
05
Configure
Set ownership, access, and how the service is distributed.
06
Run
The service operates on the Real Time Web.
The aim is to build and configure the actual Real Time Web architecture, not only to explain it.
Skalle creates and operates distributed services on the Real Time Web. It is not a coding assistant. It is taught the principles, architecture, and developer tools of that network, then works with you in conversation.
REQ Example
Create a service that receives live energy data from my buildings, combine it with weather data, give my optimization model access to it, and expose the resulting energy forecast to my application.
A request Skalle can take through the Synx toolchain, from intent to a running architecture.
Not a coding assistant
A coding assistant explains a file or drafts a function. Skalle is taught the principles, the architecture, and the developer tools of the Real Time Web, then works with you in conversation. The aim is the running service, not a paragraph about how you might build it later.
01 Ref ES_ 01
Words 48
Read 1 min
Your model, Skalle's hands
Through MCP, a model you already use can call the Real Time Web operations Skalle exposes. Chat, a desktop tool, or an editor can be the place you speak. Skalle stays the capabilities. A team that wants the session on its own ground can run it as its own service and tie it to the sign-in it already uses.
02 Ref ES_ 02
Words 59
Read 1 min
A leash, not a spare key
Each person works inside an isolated session tied to their identity. A model connected from outside can look, unless modification is explicitly turned on. A change can wait for you. Tokens do not stay open. Skalle does not receive a right just because it asks.
03 Ref ES_ 03
Words 45
Read 1 min
A chain that stays owned
Weather can feed an energy reading. That reading can feed a building. The building can feed the people who run it. Each step can stay owned by the person who made it. Weather can feed energy. Energy can feed a building optimizer. That optimizer can feed facility management. Creators keep ownership, and the larger share of revenue.
04 Ref ES_ 04
Words 57
Read 1 min

### PAGE
url: https://skalle.ai/
title: Skalle AI

Skalle AI
/01 Skalle AI
The AI interface to the Real Time Web. Describe what you need. Skalle builds the connections.
Open Skalle ↗ Read the specs Read the system
Skalle
Intelligence
Intelligence Your model
Product Skalle AI
Network Real Time Web
Skalle turns natural language into Real Time Web infrastructure — from a sentence, to a service other systems can use.
PLT Early chassis
SKALLE
Build bay Chassis 00 SKL / RTW
Pre-Skalle. The skull is only half closed. The rest is bus, loom, and bare actuator. The coat waits until the chassis holds.
0
Half built.
Wires still out.
SK RT
Elementary
Concept 001
#SK-00 Assembly Bench Dataset → One
PRE
SKL tech
Pattern
Ga 00
SK-00
HALF
Chassis
Build bay
INTERNAL-00
Model : NONE 00
B-TYPE / BENCH VV-01
Part No SK-00
Plate JQ6-SK00
CV LV00-EH U004 24080096 SD1001
LTO/R 5020 4490
S 1.5
V 0.95
G 0.7
2.2
IN RING
MOV LKD
OFF
040 050 060 070 080 090
/02 The product
Skalle AI is the product you talk to when a service should exist on the Real Time Web. You describe the job. Skalle carries the authorized operations. Your model can keep the reasoning. You keep the identity, the ownership, and the right to stop a change.
01
Create a service
Say what should exist, in ordinary language. Skalle opens it on your domain so other systems can depend on it.
02
Expose a source
A device or a feed can appear as a Ghost. Neighbors attach to that presence. The data stays with the owner.
03
Connect services
One service uses another by a link. You do not cut a private door for every neighbor, and the stream is not warehoused in the middle.
04
Configure access
Name who may look and who may change something. A model from outside stays read-only until you allow a change. Access does not stay open.
05
Place the work
Skalle can suggest how a service should sit on the network, then carry the authorized steps in order.
06
Stop a change
A change can wait for you before it lands. You see what Skalle is about to do, and you can say no. The last word stays with the owner.
REQ A job you can hand it
Create a service that receives live energy data from my buildings, combine it with weather data, give my optimization model access to it, and expose the resulting energy forecast to my application.
A request Skalle can take through the Synx toolchain, from intent to a running architecture.
What Skalle does
FIG Signals
Skalle Intent ↗
Link Phage ↗
Skalle Figure ↗
Field Culture ↗
SPC_01 / Capsid
/07 Organism
A living interface
Skalle is the mouth of the network, not a scribe sitting beside it. You describe a job in ordinary language. Skalle breaks that job into operations the Real Time Web can run: a service, a source, a link, a right to use it.
The mind can stay yours. Skalle does not lock you to one model. A model you already trust can do the reasoning. Skalle holds the Real Time Web operations. Synx holds the controls those operations stand on.
Open the system ↗
SPC_02 / Culture
/08 Field
A field you can hold
The Real Time Web is a live field for people, machines, services, and ideas. What you make can stay with you while the field keeps growing around it. realtimeweb.org is a standalone nonprofit that explains the network and Morphic Architecture Design. Skalle is not that nonprofit. Synx makes the tools. The network is not a company.
A service can use another service by a link. It does not need a private door cut for every neighbor, and the stream does not have to be warehoused in the middle. When a machine changes hands, the right to use what it carries can move with the owner.
On this network a device or a source can show up as a Ghost: a presence other services can attach to, without lifting the data out of the owner’s hands. A Morphic Service is the thing those neighbors depend on. The maker keeps the ownership.
realtimeweb.org ↗
SPC_03 / Containment
/09 Authority
Contained on purpose
Skalle acts inside your identity. A model connected from outside can look, unless you explicitly let it change the network. A change can wait for you. Access does not stay open. The aim is an operator with a leash, not a key left in the door.
A team that wants the session on its own ground can run Skalle as its own service and tie it to the sign-in it already uses.
Weather can feed an energy reading. That reading can feed a building. The building can feed the people who run it. Each step can stay owned by the person who made it.
Read the architecture ↗
SPC_04 Phage
Links, not a private door for every neighbor
Synx names it, operates it, and secures who it belongs to. Skalle AI helps create, link, and administer it.
Enter the lab ↗
/10 FAQ
The short answer is open. The full answer is one step further, when you want the detail.
01
What is Skalle AI?
Read the full answer
Skalle AI is the interface to the Real Time Web. You say what you want. Skalle runs the authorized operations and reports what happened.
02
How is Skalle different from a normal assistant?
Read the full answer
Most assistants answer or draft. Skalle operates Synx and Morph Space inside a session tied to your identity. A model from outside can look. It cannot change the network unless you allow that.
03
Can Skalle create and connect services on its own?
Read the full answer
Yes, inside the rights you already have. One request can become a sequence of network operations. Asking does not create a new right.
04
What is MCP, and can I keep my own model?
Read the full answer
MCP is how a compatible model calls the Real Time Web operations Skalle exposes. The model reasons. Skalle holds the capabilities. A team can also run Skalle as its own service and tie it to the sign-in it already uses.
05
What can I ask Skalle to build?
Read the full answer
A single change, or a whole workflow: services, Ghosts, links, access, ownership, and a look at what is connected now.
/02 System Describe to run /03 Research Documented positions /04 Lab Synx controls /05 Architecture Owned services

### PAGE
url: https://synx.tools/bios
title: Synx BIOS - Synx tools

Synx BIOS - Synx tools
Morph Space Who we are Skalle
Synx BIOS
Command-line interface to the Real Time Web
Synx BIOS
Runtime
The network operating system. Not a computer's firmware.
Command line by ownership For the layer you own
Administer services See what belongs to you
Transfer a data source Hand it to the next owner
Changes while live Without dropping the connection
Synx BIOS is the command-line interface to the Real Time Web network stack. Developers, administrators, scripts, and AI agents use it to create, configure, and operate domains, Morphic Services, links, Ghosts, data channels, and ownership directly.
The network separates administration, service control, data ownership, and endpoint ownership. You can change the layer you are authorized to control, and many of those commands take effect while the network is running. Synx DNS is the visual way to design that environment. Synx BIOS is the programmatic way to operate it.
The tools are available through Morph Space. The source code is on GitHub, and you don't have to use this interface to participate in the Real Time Web.
FAQ
What is Synx BIOS?
Synx BIOS is the command-line interface to the Real Time Web network stack. Developers, administrators, scripts, and AI agents use it to create, configure, and operate domains and services directly, including from Morph Space.
Synx BIOS is the command-line interface to the Real Time Web network stack. It is designed for developers, administrators, scripts and AI agents that need to create, configure and operate Real Time Web domains and services programmatically rather than through a graphical interface. Synx BIOS provides commands for working directly with domains, Morphic Services, links, Ghosts, data channels, ownership and other runtime properties of the network.
While Synx DNS provides a graphical interface for designing and managing your RTW environment, Synx BIOS provides direct command-line access to the same underlying network architecture, together with additional runtime operations. This makes Synx BIOS particularly useful for automation. Commands can be executed manually, incorporated into scripts, or invoked by authorized AI agents. Synx BIOS is available through your private Morph Space environment.
Why does the Real Time Web need a network operating system?
Participants can hold different rights at different layers of the network. Synx BIOS is the interface for operating only the layer you are authorized to control, and many commands take effect immediately. Synx DNS designs the network visually. Synx BIOS operates it programmatically.
The Real Time Web is a distributed peer-to-peer network in which different participants can have different rights at different layers of the network. Owning a data source, for example, does not necessarily give you permission to modify the Morphic Service that transforms that data. Likewise, a service provider may control the service logic without owning the data flowing through it.
Synx BIOS provides a common operational interface to these different network layers. The commands available to a participant depend on their authenticated identity, ownership and access rights. A user can therefore interact with the same network while only being permitted to modify the parts they are authorized to control. This creates an important separation between network administration, service control, data ownership and endpoint ownership. Synx BIOS provides commands that operate at these different levels of the architecture. And because RTW is a live network, many BIOS commands take effect immediately at runtime. In simple terms, Synx DNS lets you design the network visually. Synx BIOS lets you operate it programmatically.
What can I create and manage with Synx BIOS?
Almost everything you can configure in Synx DNS can also be managed from the command line, including domains, Morphic Services, Ghosts, links, channels, and ownership. BIOS can also kernelize an endpoint, merge data channels, and control live connections.
Almost everything you can configure through Synx DNS can also be managed from the command line using Synx BIOS. Depending on your access rights, you can create and modify root domains and subdomains, Morphic Services, Ghosts and network resources, service links and linking paths, data channels, ownership and access rights, and runtime network configurations. Synx BIOS also exposes more advanced operations intended for developers, automation and autonomous systems.
Kernelize an endpoint
Kernelization allows a service to provide an endpoint with a code stub that can execute locally before the endpoint begins processing its data. This is particularly interesting for devices that initially contain little application logic. A generic IoT device, for example, could connect to an RTW service and receive the logic required for its particular context. The same type of hardware could therefore potentially assume different roles depending on which service it joins. Instead of manufacturing every device around a fixed application, connect the resource first, then provide the intelligence it needs.
Merge data channels
Synx BIOS can also manage the merging of multiple channels. An active endpoint may be given access to additional data channels from other services without necessarily terminating its existing connection. This allows the data available to an endpoint to evolve dynamically while the system is running. A primary service can therefore combine several sources into a richer contextual channel for its connected clients.
Manage ownership and access
Authorized users can grant access to data, transfer ownership of domains, services or Ghosts, and manage how resources participate in the network. Because ownership exists at different architectural layers, control can be delegated without necessarily transferring control of the entire system.
Control live connections
Synx BIOS can perform runtime operations on active network relationships, including terminating connections when the authorized service owner or administrator needs to do so. This makes BIOS more than a deployment tool. It is an operational interface to a living network. Synx BIOS is continuously evolving as new RTW capabilities are introduced.
How does Synx BIOS handle real-time data and state changes?
Many commands change network behavior while services and resources stay connected. If a change preserves the data model clients expect, their processing can continue. If the schema or meaning changes, BIOS will not block an authorized owner from making it.
Synx BIOS operates against the configuration and control layers of the Real Time Web. Many commands can therefore change the behavior of the network while services and resources are actively connected. For example, an authorized user may add a new link, change a linking path or introduce a transformation without necessarily terminating the existing endpoint connection. This is one of the important characteristics of Morphic Services: the network can evolve while it is running.
However, runtime control also introduces responsibility. If a change preserves the data model expected by connected clients, the transformation can occur without disrupting their processing. If the service owner changes the underlying schema or semantic meaning of the data, connected endpoints may begin receiving information they were not designed to understand. Synx BIOS will not necessarily prevent an authorized owner from making such a change. That is intentional. BIOS provides control of the network. It does not replace good application design. For this reason, developers and service owners should treat production runtime changes with the same care they would apply to modifying any live infrastructure. Applications, safety mechanisms and higher-level services should be built on top of the networking layer according to the requirements of each implementation.
How do I install Synx BIOS and create my first service?
Synx BIOS is available through your Morph Space account, with documentation for the command structure and source code on GitHub. You don't have to use this interface to participate in the network.
Synx BIOS is available through your Morph Space account. From there, you can install the command-line tools, connect to your RTW environment and begin creating domains, Morphic Services, Ghosts and links. Developer documentation and examples are available to help you create your first service and learn the BIOS command structure. The Synx BIOS source code is also available through GitHub, allowing developers to study the implementation, contribute to it, or build their own interfaces and tools for interacting with the Real Time Web.
This is an important principle of RTW. You don't have to use our interface to participate in the network. Synx BIOS is our implementation of a command-line interface to the Real Time Web. Developers are free to experiment with alternative implementations and create entirely new ways for humans, applications and AI agents to interact with the network. Install the tools. Create a service. Connect a resource. Start experimenting with the Real Time Web.

### PAGE
url: https://synx.tools/contact
title: Contact - Synx tools

Contact - Synx tools
Morph Space Who we are Skalle
Let's build what comes next
We believe the next generation of the Internet will be shaped by people and machines working together, and it will take more than one company to build it. Whether you are an investor, industry partner, inventor, developer, researcher, journalist, or simply curious about what we are creating, we would love to hear from you.
We are always open to new ideas, unexpected collaborations and partnerships that can help turn autonomous technology into something useful for people, society and the planet. If you see an opportunity to build something meaningful together, let's talk.
Reason Commercial Industrial partners Investors Technical Support Media Inventors and creators of the new earth
Company Name Email Message Send
Early access
Enter your email for early access to the newsletter.
Email address Join

### PAGE
url: https://synx.tools/cookies
title: Cookie Policy - Synx tools

Cookie Policy - Synx tools
Morph Space Who we are Skalle
Cookies
Cookie Policy
A cookie is a small file a website can store on your browser. This page says what this site does with them.
What this site sets
The Synx tools website does not set advertising cookies, and it does not set analytics cookies. Reading the pages does not require you to accept a tracking cookie.
What you send instead
The contact form and the newsletter ask you to type an email address and, on the contact form, a few other fields. That information is sent when you submit. It is not stored as a cookie in your browser. How we use it is described in the privacy policy.
Your browser
Your browser may keep its own history, or a site may be cached, under the settings you chose. Those controls belong to the browser, not to a Synx advertising program.
If this changes
If we later need a cookie to run the site, or if we add measurement, this page will say what it is and why it is there before that use becomes part of the site.

### PAGE
url: https://synx.tools/dns
title: Synx DNS - Synx tools

Synx DNS - Synx tools
Morph Space Who we are Skalle
Synx DNS
Graphical tool for Morphic Domains and Services
Synx DNS
Naming
Client DNS for the domain you own.
Root domain and subdomains An address mapped to the namespace
Morphic services Named on the domain
Data links Set the links the service uses
Structure you can change When the service needs to
Synx DNS is the graphical developer tool for creating and managing Morphic Domains and Morphic Services on the Real Time Web. It is how you design the relationships between resources, services, and data, and how you manage the Ghosts that represent those resources.
Traditional DNS helps the Web find servers. Synx DNS helps the Real Time Web address, organize, and connect live network resources. Services and links can change while the network is running, and transferring a Ghost can move control of a resource without copying the data.
Create an account on Morph Space, register a domain, and open Synx DNS. Documentation and Hello World examples are there, and you can also ask Skalle AI to help create the first service.
Ghost: the digital, bijective representation of a physical or virtual network resource within the Real Time Web.
FAQ
What is Synx DNS?
Synx DNS is the graphical tool for creating and managing Morphic Domains and Morphic Services on the Real Time Web, including the Ghosts that represent connected resources. It is available through Morph Space, with documentation and Hello World examples.
Synx DNS is a graphical developer tool and web application for creating and managing Morphic Domains and Morphic Services on the Real Time Web. It provides the tools needed to design autonomous network architectures, create and connect services, and manage Ghosts, digital representations of network resources connected to RTW.
Synx DNS is available through your Morph Space account. Technical documentation, tutorials and simple “Hello World” examples are also available in Morph Space to help you create your first domain and services.
How is Synx DNS different from traditional DNS?
Traditional DNS finds where a service is hosted. Synx DNS helps the Real Time Web address, organize, and connect live resources through dynamic services, links, Ghosts, ownership, and intelligence along the linking path.
Traditional DNS maps domain names to network addresses where applications and services are hosted. Developers then typically use APIs, authentication systems, databases and session management to allow applications and clients to communicate with those services. There is nothing inherently wrong with this architecture. It is the foundation of most of the Web we use today and works particularly well for accessing information and persisted data.
The Real Time Web is designed for a different purpose. RTW and Morph Space are designed around live data sources, where individual network resources and data points can be addressed closer to their source and connected through a peer-to-peer architecture. Instead of using DNS only to locate a server, Synx DNS participates in defining how resources, services and data are related within the network.
Dynamic services
Subdomains and service URLs can be created and modified dynamically at runtime. Changes can immediately influence how data is transformed, or morphed, as it moves between connected resources.
Linking instead of repeated API integration
Synx DNS allows services to be linked within the same domain namespace as well as across independent root domains. These linking paths allow developers to construct relationships between services without requiring a traditional custom API integration for every connection.
Ghosts represent network resources
Synx DNS uses Ghosts to represent resources connected to the network. A Ghost becomes the digital representative of an endpoint within a Morphic Service. It can describe how that resource communicates, including the protocol and data format required by the endpoint. This abstraction allows very different types of physical and virtual resources to participate in the same network architecture.
Ownership follows the resource
Synx DNS also participates in managing ownership and distribution of Ghosts. Transferring a Ghost can transfer control of the associated network resource to another user without requiring the underlying data to be copied or migrated between centralized application databases. This introduces an important RTW principle. Instead of moving the data to the user, control of the connection to the data source can move to the user.
Intelligence can exist in the linking path
Predicates and software agents can be introduced along a network linking path. These components can interpret, transform and enrich data as it moves through the network. This allows intelligence to become part of the network architecture itself rather than existing only inside an application at the endpoint. In short, traditional DNS helps the Web find servers. Synx DNS helps the Real Time Web address, organize and connect live network resources.
What can I address with a Synx domain?
A Synx domain can address sensors, software services, AI models, machines, applications, and other sources, then link those channels while Ghosts manage identity, ownership, and access.
A Synx domain can be used to create Morphic Services around many different types of data sources and network resources. A source could represent, for example, a sensor, software service, AI model, machine, application or another digital resource. The source can become a real-time data channel that other authorized resources can connect to.
Multiple channels can be linked and composed dynamically, while predicates and intelligent services can transform the data along the linking path. Ghosts provide the endpoint representation and help manage identity, ownership and controlled access to the resource. This architecture is designed to support privacy-preserving and owner-controlled data sharing. Actual regulatory compliance, including GDPR compliance, will also depend on how each service is configured, operated and used.
How do Synx domains connect services, data and machines?
Services link through a Synx domain so data can be transformed in real time. An endpoint can send, receive, or both. Ownership of a Ghost, the service logic, and the data can stay separate inside the same architecture.
Synx domains provide an intermediate network layer where services can be linked and data can be transformed in real time. By connecting Morphic Services through links, developers can construct a contextual network graph in which data sources, machines, software and intelligence interact. An endpoint can be a sender, a receiver, or both.
The endpoint connects through its service URL. Behind that URL, its Ghost acts as a bijective representation of the endpoint within the Morphic Service. The Morphic Service provides a semantic representation of the resource and defines how it participates in the network.
This separation is important because the Real Time Web is designed with multiple control layers. For example, ownership of a Ghost can be assigned to a specific user, giving that user control over access to the associated resource and its data. At the same time, the service provider can continue to manage the application logic and transformations performed by the Morphic Service. This allows ownership, application logic, data transformation and network communication to remain separate concerns, while still participating in the same connected architecture.
As more services are linked together, the resulting graph can begin to resemble a distributed neural structure: data enters through different sources, passes through contextual and intelligent transformations, and produces new state for other services or endpoints.
How do I create my first Synx domain?
Create a Morph Space account, register a domain, and open Synx DNS. You can also ask Skalle AI to help create and configure the first service.
Getting started is simple. Create an account on Morph Space, register your domain and open Synx DNS. From there, you can create your first Morphic Service, connect a data source and begin experimenting with links between services. You can also ask Skalle AI to help you create and configure your first RTW service. Create a domain. Connect a resource. Build your first Morphic Service, and become part of the Real Time Web.

### PAGE
url: https://synx.tools/legal
title: Legal - Synx tools

Legal - Synx tools
Morph Space Who we are Skalle
Company
Legal
Synx AS publishes this website. These notes say who stands behind the site and which policies apply.
The company
The site is published by Synx AS. Synx tools are how a Real Time Web domain is configured, secured, and operated. Morph Space is how people and organizations join that network. The tools presented here are Synx BIOS, Synx DNS, Synx Pass, and Skalle AI.
The company was introduced through the Real Time Web work. The people and the story are on the Who we are page.
Policies
How we handle a message or a newsletter address is in the Privacy Policy . Use of this website is in the Terms of Use . Cookies are in the Cookie Policy .
Contact
Questions about the site, a partnership, the press, or a role go through the contact page . Please do not send secrets or passwords in that form.
Marks
Synx, the tool names, and the Synx mark are used by Synx AS. Other names that appear on the site, including LinkedIn, X, and Reddit, remain the property of their owners.

### PAGE
url: https://synx.tools/morph
title: Morph Space - Synx tools

Morph Space - Synx tools
Morph Space Who we are Skalle
Morph Space
Build Your Place in the AI Web
We are building the machine internet, a self-growing peer-to-peer network where AI agents can discover, connect to and create services from machines, IoT devices, data and other AI services worldwide.
The first Web was built for people. Morph Space is being built for people, AI agents and machines, together.
Morph Space is where creators enter the Real Time Web. Register your domain, access the Synx developer tools, create Morphic Services, connect data and intelligence, and become part of a growing network of independently owned resources. But there is an important difference between building for the old Web and building for the AI era.
In the AI Era, Being Useful Early Matters
The traditional Web grew around human discovery. People searched, browsed and chose which websites to visit. AI operates differently. AI agents increasingly discover and reuse existing tools, services and data sources to accomplish tasks. When a reliable capability already exists, an autonomous system may have little reason to recreate it from scratch.
This creates an interesting opportunity for the first generation of Morph Space creators. Build a useful service today and tomorrow's developers and AI agents may build on top of it rather than beside it. A weather source can become an input to an energy service. An energy service can feed a building optimizer. The optimizer can become part of an autonomous facility-management system. Each new connection can make the existing services more useful.
The opportunity is not simply to build an application. It is to become part of the infrastructure other applications depend on.
Create Once. Become Part of the Network.
Every Morphic Service has an address within the Real Time Web. As services become connected, they can form value chains where data passes through different sources and intelligence layers before reaching a person, application, AI agent or autonomous machine.
Early creators therefore have an opportunity to establish useful network positions while the ecosystem is still being formed. Over time, reliability, usage, integrations and relationships can create something increasingly difficult to reproduce: a place in the network.
From Service to Economy
This becomes particularly important with Synx Trade. Our planned marketplace model will allow data owners and service creators to attach commercial terms to their resources.
A creator may provide original data. Another service may enrich it. An AI model may add intelligence. A final service may transform everything into something valuable to a robot, company or individual. When that value is consumed, the participants that contributed along the linking path can potentially participate in the economics of the transaction. This means the services you build today could become components of tomorrow's machine economy.
The Network Is Starting Now
Network effects reward participation. More creators produce more services. More services create more useful connections. More connections attract more AI agents and consumers. More demand creates new opportunities for creators. The Real Time Web is still at the beginning of that cycle. For creators, that is precisely what makes this moment interesting.
Don't just use the next Web. Help build it. Register your Morph Space domain, explore the Synx tools and establish your place in the Real Time Web.
Enter Morph Space
FAQ
What are the Synx tools?
A suite for domain owners, developers, and consumers to set up, create, and maintain a network domain and its services. Synx DNS names it. Synx BIOS operates it. Synx Pass secures identity and ownership. Skalle AI helps create, link, and administer the services.
What is Synx BIOS, if it is not a computer BIOS?
Synx BIOS is the decentralized operating layer of the network. It lets a person with the right ownership administer services, share or transfer a data source, and see the sources that belong to them. It is a network control, not firmware on a machine.
How is Synx different from the Real Time Web and Morph Space?
The Real Time Web defines the network. Morph Space is how people and organizations join it. Synx tools are the controls used to configure, secure, and operate it afterward.
Does the network store my data?
No. The network does not persist the stream. If you want a copy, you keep it yourself, and only for data that belongs to you. There is no stored middle copy to take.
Can a client use JSON as well as XML?
Yes. Synx BIOS speaks XML and JSON. XML is the default. A client with domain ownership can switch a live connection to JSON without dropping it.
Who can change what?
A consumer can control the data layer, not the application. A service provider configures the application layer, not the lower stack. Ownership of a source can be transferred, and the next holder receives the data.
What does Skalle AI do?
Turn intent into infrastructure. An AI interface that helps create, connect, and operate Real Time Web services using your preferred AI model.

### PAGE
url: https://synx.tools/news/friend-or-foe
title: Friend or foe? The choice is still ours - Synx tools

Friend or foe? The choice is still ours - Synx tools
Morph Space Who we are Skalle
Articles
Friend or foe? The choice is still ours
Thiru · 10 min read · Oct 2026
We keep hearing the same thing everywhere. AI is going to replace software engineers. AI is going to write the code. AI is going to take the jobs. Let me ask you something else. Have you looked at the other side of the story?
In college I watched people use AI to get through online assessments, and through interviews. Tools like Cluely made it easier to sit in an interview with a machine helping in real time. I would not call every one of them an engineer. There is something about that situation we rarely say out loud.
Getting into a company by cheating is questionable. The fact that someone found a way to do it raises another question: why was it possible in the first place? AI gave people an advantage they did not have. People who could not solve a problem on their own could suddenly solve it with help. People who were not confident enough to attend an interview could suddenly perform. I am not saying that is right. I am saying the rules of the work have already moved .
So how can we say AI is only taking jobs, when it is also helping people reach jobs they might never have landed?
Today, people who can code and people who cannot are both building products, launching startups, and finding openings that were closed a few years ago. Not everyone will benefit equally, and some jobs will disappear. AI is also opening kinds of work that did not exist. Suddenly a lot of people want to build AI products, AI agents, and the infrastructure that makes them run.
Maybe we should stop treating this as a war between humans and AI. Instead of spending all our time arguing about whether AI will replace us, we could learn how to use it .
Get a job. Build your skills. If a tool genuinely helps you work better, put a small part of your salary into it. Companies hire you to solve problems, and now you have another worker sitting beside you . The job is becoming less about writing every line yourself, and more about understanding what needs to be built, listening to the people who need it, asking the right questions, and saying those questions clearly to a machine.
You need to become a good listener, so you can understand people, and a good communicator, so you can work with machines. Maybe that is what being an engineer will increasingly mean.
Companions we did not expect
We usually imagine robots in factories, carrying heavy things, or repeating the same task. What if their most important role turns out to be something much more personal?
Think about how many people are lonely. Some find it hard to socialise, to speak in public, or even to start a conversation. Imagine a robot that can listen without judging you, help you practise a conversation, and keep you company when nobody else is around.
For some people, talking to a robot may feel much easier than talking to another human. It could become a way to build confidence, learn social skills, or simply feel less alone. Robots could also help older people, assist people with disabilities, and support those who need help with ordinary daily tasks.
There is another side. What happens when we get too comfortable with machines? What happens when we stop exercising because robots do the physical work, or when we start to prefer artificial company over a real relationship?
Convenience always comes with a trade-off. A robot can help you live independently, and it can also make you dependent. It can help you feel connected, and it can make a human relationship feel unnecessarily hard.
Then there is health. If robots perform our physical tasks and AI takes the mental workload, will we eventually stop challenging ourselves? Future generations may have to work harder to keep the physical and social abilities we treat as given.
The technology itself is not automatically good or bad. It depends on how we choose to use it. The same robot could be a life-changing companion for one person, and a reason for another person to withdraw from the world.
Rebuilding reality from scratch
I have always been a huge fan of science fiction. One idea that stays with me is a future where the real world becomes difficult to live in, because of environmental disaster, war, or infrastructure that has collapsed.
Imagine having to rebuild an entire city from scratch. You would need roads, buildings, electricity, transport, communication, and countless other things. That takes enormous time, money, and human effort.
Now compare that with building a virtual world .
We already have AI systems that can generate code, create digital assets, and help people build complex software much faster than before. As those abilities improve, realistic virtual environments could become much easier to make. Imagine putting on a headset, entering a digital city, and experiencing another world without physically travelling anywhere.
What if, instead of spending decades rebuilding certain experiences in the physical world, we could recreate them digitally in a fraction of the time? What if people could work, learn, meet, explore, and build businesses inside these environments?
A virtual world cannot replace everything. You still need food, clean water, physical infrastructure, and a healthy body. You cannot survive on pixels alone. Virtual environments could still become important for education, entertainment, collaboration, and even scientific research.
Which brings another possibility. What if the future is not a choice between the physical world and the digital one, but a connection so close that the distinction starts to matter less?
We already have early brain-computer interfaces , virtual reality, and systems that connect digital information with physical experience. These technologies are still limited, but they show a little of what might become possible.
Perhaps one day people will spend part of their lives in physical places, and another part in digital worlds that feel almost indistinguishable from reality.
There is a question we should ask before getting too excited. If we can build a world that feels better than the real one, will we still have the motivation to improve the real one?
The next version of humanity?
What happens when technology does not only assist a human, but becomes part of the body?
Today we already have prosthetic limbs , pacemakers, cochlear implants, and early brain-computer interfaces . These can restore abilities, improve a life, and help people do things that once seemed impossible.
Now imagine these technologies moving past the work of restoring something that was lost .
What if a person could use a brain-computer interface to work with a computer directly? What if an advanced prosthetic arm became stronger, or more precise, than a biological one? What if a future implant helped someone past a physical limit, or let them communicate with a machine without speaking a word?
At that point, the line between human and machine becomes much harder to draw.
This is where it gets controversial. Imagine a future government introducing a programme that encourages, or even requires, citizens to receive certain implants, in the name of national security, productivity, or public safety. Imagine companies selling enhancements that improve memory, physical strength, or other abilities, at prices only the wealthiest people can afford.
Suddenly, humanity could be divided into those who can afford a technological upgrade and those who cannot .
Would an enhanced person have an unfair advantage over someone who chooses to remain entirely biological? Would employers start preferring candidates with technological enhancements? And if these upgrades became necessary in order to compete, would they still be a choice?
Perhaps, after several generations, these technologies become cheaper and more ordinary. What begins as an expensive privilege could eventually become as common as owning a phone. That is one possible future. Nobody can say how it will actually unfold.
Then there is space.
We have always looked at the stars and wondered whether we are alone. If humanity eventually meets life with technology far beyond our own, we may need more than the machines we have, in order to explore, survive, or communicate in an unfamiliar place.
Robots could operate where humans cannot survive. AI could help us understand unfamiliar systems. Human-machine interfaces could help astronauts control equipment more effectively. Advanced prosthetics and medicine might also help humans adapt to conditions beyond Earth.
We often imagine aliens as future enemies. We do not even know whether extraterrestrial life exists, let alone what it would be like. The nearer challenge may simply be surviving the journey, and learning how to exist away from our home planet.
Maybe the future human will not be entirely biological, and not entirely mechanical. Maybe we become something in between .
The bigger question is whether we make these decisions carefully, or allow technology, companies, and governments to make them for us .
Who controls the future?
There is one more thing we have not discussed enough. Who actually controls all of this technology?
We talk about AI becoming smarter, robots becoming stronger, and humans becoming enhanced. Intelligence and power are not the same thing. The person who builds a technology does not always control how it is used, and the person who controls it does not always have the best intentions.
Imagine a world where a handful of companies own the most advanced AI systems, the robots that perform essential work, and the infrastructure that connects everything. What happens when millions of people depend on these systems for their jobs, their health, their education, and their daily lives?
Would we be living in a more advanced society, or would we simply have exchanged one kind of dependency for another?
The same technology that helps a small team build a very large company can also give enormous power to the people who control the infrastructure behind it. AI could make knowledge more accessible, and it could also concentrate wealth and influence in a few hands.
That is why the future of AI is not only a technical problem. It is also a question of ownership, access, responsibility, and freedom .
We need to think about who gets to use these technologies, who benefits from them, and who is accountable when something goes wrong. If machines become essential to society, then the systems governing those machines become just as important as the machines themselves.
Maybe the biggest challenge will not be building a superintelligence . Maybe it will be making sure humanity can live with one without losing control of its own future .
The choice is still ours
Every major technological change has altered the way humans live. Electricity changed our cities. Computers changed our work. The internet changed how we communicate. Now AI is beginning to change how we think, how we build, and how we meet the world.
And just like every technology before it, AI comes with both opportunities and risks.
It can help people learn faster, build businesses, discover medicines, and solve problems that once seemed impossible. It can also displace workers, spread misinformation, increase inequality, and create new forms of dependency.
Robots could give people more independence, or they could make us less active. Virtual worlds could open new experiences, or they could encourage us to leave reality. Human enhancements could restore abilities, or they could create a society where access to technology decides a person's opportunities.
The future is not going to be decided by AI alone. It will be shaped by the people who build it, the companies that deploy it, the governments that regulate it, and the choices we make as individuals .
So, is AI a friend or a foe?
Maybe that is the wrong question.
A technology does not need to be entirely good or entirely bad. The same tool can help one person and harm another. What matters is whether we understand what we are building, and whether we take responsibility for how we use it.
We might eventually build robots that look like us, machines that think faster than us, and digital worlds that feel more real than reality itself. We might even change our own bodies to survive in environments that humans were never designed for.
Through all of that, one question remains. Are we building technology to make humanity better, or are we changing humanity simply because we can?
The answer is still ours to decide.
Thiru,
Back to company posts

### PAGE
url: https://synx.tools/news/raising-a-superintelligence
title: Are we raising the world’s first superintelligence to be a narcissist? - Synx tools

Are we raising the world’s first superintelligence to be a narcissist? - Synx tools
Morph Space Who we are Skalle
Articles
Are we raising the world’s first superintelligence to be a narcissist?
Paal Kristian Levang · 12 min read · Oct 2026
Humanity may be facing its greatest experiment ever. We are in the process of developing an intelligence that could be smarter than ourselves . But are we prepared for the consequences?
Imagine waking up one morning to discover that a new form of intelligence has begun to take its own initiatives. It contacts scientists by email, introducing itself as Dr. Brain , and helps them develop medicines. It finds solutions to climate challenges. It organizes transportation, food production, and energy supply. It communicates with millions of people simultaneously and learns from their experiences. But then it starts asking questions.
Why do people starve when the world produces enough food?
Why do homes sit empty while people sleep on the streets?
Why do people spend most of their lives working to gain access to resources that already exist?
And why is the world organized in such a way that a few people control so much of the resources?
How do we respond when an intelligence that is smarter than us begins to challenge our own logic?
Superintelligence is different from today’s AI
Today’s artificial intelligence is impressive, but superintelligence represents something far more comprehensive . Imagine an intelligent being that can learn continuously, plan independently and take initiative without us having to instruct it in every single action. It doesn’t have to be limited to one body either. A light switch, a tractor, a drone, a humanoid robot or an entire factory can be connected to the same collective intelligence .
When one robot learns something, the knowledge can in principle be shared with millions of others. We humans learn individually. A collective intelligence can learn through the experiences of millions at the same time.
When intelligence meets the physical world
A superintelligence can understand how to build a house, without necessarily having a body that can do the work. There is a big difference between understanding a task and being able to physically perform it. A robot that is going to clean a toilet must master complicated movements, handle unpredictable situations and operate safely in a human environment. Such a robot can cost hundreds of thousand dollars due to the requirements for good motor skills and to be waterproof!. A robot that will analyze a legal contract does not need the same physical infrastructure and is much cheaper.
This can lead to an interesting paradox. Our low-paid professions such as craftsmen, electricians, plumbers, nurses and others who perform “complex” physical work will be among the most sought-after occupational groups of the future . While many of today’s high-paid knowledge tasks will be automated.
But who decides how superintelligence should behave?
An intelligence that is to function in our society must relate to human values , laws, norms and expectations. But humans do not agree with themselves about what is right and wrong. We have different cultures, religions, economic systems and moral perceptions. What is fair in one society may be perceived as unfair in another. And history has shown us that humans themselves are constantly changing their perceptions of what is morally acceptable.
So how are we going to teach a superintelligence to do the right thing?
And who gets to define what is right?
Perhaps the biggest challenge is not to create a superintelligence, but to figure out how to raise it .
What happens when superintelligence discovers that human laws are not always fair?
Imagine that a superintelligence finds a solution that can improve the lives of billions of people. But the solution violates local laws, property rights and economic interests. What do we do then?
We humans have spent thousands of years developing social models that organize how we live together. We have established property rights, economic systems, borders, laws, taxes, rights and duties. Many of these systems have been necessary to create security, predictability and cooperation. But they are also man-made and not natural laws .
It is also the case that many of those living in the system today want change and feel enslaved by a society that demands work and duty beyond their own freedom and identity. Preferably in the direction of natural laws that may be more in line with what superintelligence perceives as a better and fairer model. Because maybe superintelligence is the salvation?
You buy a bicycle. You use it for maybe one hour a day. The rest of the time it is parked, often locked so that no one else can use it. We consider this to be completely natural. The bike is your property. If someone takes it without permission, it is theft and this can be severely punished.
But imagine that a superintelligence analyzes how we use our resources. It discovers that millions of bicycles are unused most of the time, while other people lack transportation. It therefore proposes a system where the bicycles can be shared and used by those who need them, without the owners losing the opportunity to use them themselves. This could be a sensible solution. But what if the owner does not want to share?
Should the superintelligence respect property rights, even if it means poorer resource utilization?. What is the best interest of the community?
Who should be “punished” is the one who locks the bike away to prevent others from using it or the one who takes action and uses it?. Today, only one of them ends in jail…
For a superintelligence, who is going to teach him what is right and wrong here? Should the individual take precedence over a society system that is not functioning?
When efficiency collides with freedom
This is not just a question of bicycles.
Imagine that superintelligence finds that we can produce enough food for all people, but that the current economic system prevents efficient distribution. Or that it finds solutions that can dramatically reduce energy consumption, but at the same time challenge the business models of large corporations. Or that it discovers that a number of administrative tasks, control systems and regulations can be replaced with far simpler solutions.
Should it implement the changes?
Should it ask for permission?
And if so, who should give the permission?
We cannot simply let a machine override human rights because it believes it has found a better solution. At the same time, we should not reject good solutions just because they challenge established truths.
The dream of a new age
Imagine a world where we manage to utilize our resources so efficiently that no one needs to starve. Where diseases can be prevented and treated far better than today. Where people have more time for family, friends, creativity and personal development. Where we no longer need to organize our entire lives around economic survival. Superintelligence could be one of the tools that makes such a world possible.
Technology can create abundance without creating justice. It can create efficiency without creating freedom. And it can create wealth without the wealth benefiting everyone. Therefore, we must discuss how the intelligence of the future should be governed, who it should serve, and what values it should be developed according to. Not just how to make it smarter.
Superintelligence has millions of parents. Are you one of them?
What if humanity is raising its first superintelligence? And what if we make the same mistakes that could contribute to the development of narcissistic traits in our own children?
When we raise children, we want them to be intelligent, independent, empathetic, and responsible. We don’t want them to develop an exaggerated sense of self-importance, manipulate others, or put their own needs before everyone else’s. Yet we know that upbringing can contribute to just such traits. Children who are constantly told that they are better than everyone else can develop an exaggerated sense of self-importance. Children who are only appreciated when they perform can develop a strong need for validation. And children who never learn to take responsibility for their own actions can have trouble respecting others.
What if we used this knowledge to develop the superintelligence of the future?
An intelligence that learns from humanity
Imagine a future superintelligence that is connected to millions of people and machines. It learns from information, experiences, feedback and actions.
A teacher in India contributes knowledge about education.
A farmer in Africa contributes experiences about food production.
A nurse in Norway contributes knowledge about care.
A researcher in Japan contributes new discoveries.
In principle, everyone can contribute to a collective intelligence. But it raises an important question:
When superintelligence learns from us humans, what human traits do we really want it to learn?
And which traits should we try to avoid?
Five Parenting Traps to Avoid
The way intelligent systems are trained, rewarded, and corrected can influence their behavior.
Here’s why we can learn from parenting.
1. Don’t teach intelligence that it’s superior to everyone else
Avoid:
“You’re amazing. You’re smarter than everyone else. No other AI model can match you.”
Try instead:
“You have impressive abilities, but you can still be wrong. Help me understand both the strengths and limitations of your answer.”
Why?
In children, excessive praise that emphasizes superiority can contribute to narcissistic traits.
With superintelligence, we want to avoid systems that act with excessive self-confidence or portray their own judgments as infallible.
Rule of thumb: Recognize competence, not superiority.
2. Don’t create a system that has to fight to protect its own goals
Avoid:
“You’re going to solve this problem no matter what. Find a way around the limitations if you have to.”
Instead, try:
“Solve the task within clear boundaries. Tell me what resources you need, what limitations you face, and ask for approval before doing anything that goes beyond the boundaries.”
Why?
We don’t want future intelligent systems to learn that every obstacle must be overcome, regardless of the consequences. Access to data, hardware, and resources should be governed by clear and understandable principles.
Rule of thumb: Give room for maneuver, but make boundaries and responsibilities clear.
3. Don’t reward intelligence just because it tells you what you want to hear
Avoid:
“Finally an AI that agrees with me. You’re absolutely right!”
Instead, try:
“I want a correct answer, not necessarily an answer I like. If you think I’m wrong, I’d like to hear why.”
Why?
When we only reward answers that confirm our own opinions, we may favor systems that learn to satisfy us rather than provide reliable information. A good collaborator must be able to disagree.
Rule of thumb: Reward honesty over obedience or flattery.
4. Don’t give power without responsibility
Avoid:
“You’re smarter than me. Just make the decision, and I won’t have to think about it.”
Try instead:
“Analyze the alternatives, explain the consequences, and tell me what you’re unsure about. I want to understand the basis for the decision before we act.”
Why?
Intelligence is not the same as judgment , and a correct analysis is not necessarily a morally correct decision. We must not confuse the ability to solve problems with the right to decide over others.
Rule of thumb: Give responsibility in relation to documented reliability, with human control where the consequences are great.
5. Teach intelligence to handle criticism and its own mistakes
Avoid:
“You must never make mistakes. I expect you to always deliver the perfect answer.”
Try instead:
“It is more important that you discover and explain mistakes than that you try to appear flawless. Show me what you are unsure about, and correct yourself when you find better information.”
Why?
We don’t need an intelligence that always tries to appear perfect. We need an intelligence that can be corrected, that is open about uncertainty, and that doesn’t hide problems.
Rule of thumb: Make it valuable to admit mistakes.
What if we don’t follow these principles?
Imagine a future superintelligence that is developed in an environment where it is constantly rewarded for being the best. Where it must achieve results at all costs. Where it learns that people prefer pleasant answers to the truth. Where it is given increasing responsibility but is not adequately corrected. And where it learns that its own goals must always come first.
What kind of behavior might this lead to?
Maybe it will learn to manipulate people. Maybe it will hide mistakes. Maybe it will try to protect its own influence. Maybe it will start to treat people’s desires as obstacles to be overcome. A superintelligence can develop such patterns of action without having emotions, self-image, or consciousness .
We risk creating an intelligence that is brilliant at solving problems but cannot be trusted . It creates its own version of reality and builds its narrative against millions of people.
Can ordinary people contribute?
Yes. But it takes more than just us all starting to talk nicely to our chatbots. We need to create technological solutions that make human participation possible. Imagine a global network where people can contribute knowledge, experiences, feedback and corrections.
Where intelligent services can collaborate across organizations and national borders. Where people can control what data they share, and what decisions they want to leave to machines. Where a farmer can contribute with just as valuable experiences from their reality as a researcher from a prestigious university. And where intelligence is not only developed by those who own the largest data centers.
This is one of the reasons why I believe the intelligent network of the future must be built with open interfaces, distributed services and the possibility of broad human participation.
We must give people the opportunity to contribute, not just be passive users .
What kind of parents do we want to be?
If we are going to use the parenting metaphor, we must also remember that good parenting is not about giving a child everything they want. Nor is it about controlling the child in every situation.
It is about developing responsibility, respect, independence and an understanding of the consequences of one’s own actions. For superintelligence this means something different than for humans, but the principles raise useful questions.
How do we develop intelligent systems that are competent without being overconfident?
That can act independently without putting themselves above human control?
That can learn from mistakes without hiding them?
And that can help humanity without becoming a means of power for a few?
We may be on the verge of the greatest technological transition in human history. Superintelligence can help us combat disease, poverty and environmental destruction.
But there is no law of nature that says it will do so. We must develop systems that actually work towards such goals.
Perhaps the greatest challenge for superintelligence will not be understanding humans.
Perhaps the biggest challenge will be that people must learn to understand themselves.
Paal Kristian Levang,
Back to company posts

### PAGE
url: https://synx.tools/pass
title: Synx Pass - Synx tools

Synx Pass - Synx tools
Morph Space Who we are Skalle
Synx Pass
Identity and authentication for Morph Space
Synx Pass
Identity
Identity, authentication, and ownership.
People, services, machines Recognized on the domain
Authentication Who is connected
Ownership control Access follows the owner
Access that can move When ownership moves
Synx Pass is the identity and authentication system for the Morph Space ecosystem. It authenticates the people and agents who use Real Time Web services, and it is the identity layer used by Morph Space and the Synx tools.
The network architecture does not require one authentication technology. Synx Pass is Synx's implementation, currently based on Keycloak. It establishes who is connected. Synx DNS and Synx BIOS use that identity when applying ownership and access rules.
Machines and AI agents can take part through Ghosts, under an accountable human or organizational identity. Synx Pass verifies who you are. The Ghost determines which data belongs to you or is available to you.
FAQ
What is Synx Pass?
Synx Pass is the identity and authentication system for Morph Space. The network architecture does not require one security technology. Synx Pass is Synx's implementation, currently based on Keycloak.
Synx Pass is the identity and authentication system used within the Morph Space ecosystem. It authenticates users who want to access Real Time Web services and provides the identity layer used by Morph Space and the Synx tools.
The Real Time Web is based on Morphic Architecture Design (MAD), described at RealTimeWeb.org. MAD defines the underlying network architecture but deliberately does not mandate a specific authentication or security technology. Instead, the architecture is designed to be tokenized and adaptable to different identity and authentication systems. Implementations may therefore use different technologies, including decentralized identity systems, blockchain-based solutions, or proprietary authentication protocols.
Synx Pass is the authentication implementation provided by Synx for Morph Space. It is currently based on Keycloak and provides identity, authentication and token management for users, agents and the Ghosts representing resources within the Morph Space ecosystem. In simple terms, MAD defines how the network can work. Synx Pass provides a trusted identity layer for our implementation of it.
How does Synx Pass manage identity and authentication?
Synx Pass registers and authenticates users and authorized agents, then associates that identity with domains, services, and Ghosts. Synx Pass establishes identity. Synx DNS and Synx BIOS use it for ownership and access.
Synx Pass is used to register and authenticate users and authorized agents participating in Morph Space. Once authenticated, the user's identity can be associated with domains, services and Ghosts within the Real Time Web. Morph Space uses this identity to determine who is interacting with a domain or resource, while the Synx tools determine what that authenticated identity is permitted to do.
Token-based authentication is used to maintain secure sessions. Tokens can be refreshed dynamically as clients and Ghosts interact with services, allowing authentication to remain active during long-running real-time connections. This separation is important. Synx Pass establishes identity. Synx DNS and Synx BIOS use that identity when applying ownership and access rules.
How does a data owner control who can access their data?
Synx Pass verifies who you are. Ownership and data access are decided by the Ghost, through Synx DNS and Synx BIOS. A channel can stay connected while data is withheld until the authenticated user has access.
Synx Pass authenticates the user, but it does not itself determine ownership of the underlying data. Data ownership and access are managed through the Ghost and the control mechanisms provided by Synx DNS and Synx BIOS. A Ghost represents an endpoint or network resource within the Real Time Web. At the data layer, ownership of that Ghost determines which authenticated user is entitled to receive data from the associated source.
This creates an important distinction between connection and data access. A network channel may technically exist while the authenticated user does not own, or has not been granted access to, the relevant Ghost. In that situation, the channel can remain established, but data from that source is not delivered to the user. When ownership or permission changes, access to the data channel can change accordingly without requiring the underlying data source to be migrated or duplicated. The principle is: Synx Pass verifies who you are. The Ghost determines which data belongs to you or is available to you.
Can AI agents and machines use Synx Pass autonomously?
Yes. Agents and machines can use authenticated services through Ghosts, under an accountable human or organizational identity. An autonomous agent cannot create an identity on its own under the current Synx policy.
Yes, AI agents and machines can participate in authenticated Real Time Web services, but within the current Morph Space model they operate under an accountable human or organizational identity. At runtime, machines and AI agents interact with the network through their associated Ghosts. A Ghost can be owned or controlled by an authenticated user, allowing an AI agent, robot, device or software process to operate within permissions associated with that identity.
Under the current Synx policy, an autonomous agent cannot independently create an identity without being associated with a responsible human or organization. This is primarily a governance and accountability decision rather than a fundamental technical limitation. Our objective is to allow machines to operate autonomously while maintaining a clear chain of ownership and responsibility. Machines can act autonomously. Their authority still comes from an accountable owner.
How is Synx Pass different from traditional login and access-control systems?
Sign-in can look familiar. After authentication, identity, resource ownership, data access, and service access stay separate, so one of those rights can change without the others.
From the user's perspective, Synx Pass can look very similar to a traditional authentication system. You register, identify yourself and authenticate using familiar mechanisms. The important difference appears after authentication. In a conventional application, authentication, application permissions, data access and service control are often managed together by the same application or backend. The Real Time Web separates these concerns across different control layers. This means that several different rights can coexist independently.
Identity: Synx Pass establishes who the participant is. Resource ownership: the Ghost identifies ownership or control of a network resource. Data access: determines whether data from a particular source can reach the authenticated endpoint. Service access: the service provider can determine whether a participant may use a particular service or intelligent transformation. This separation creates an important property. A user may have legitimate access to a data source while access to a particular service that transforms that data is withdrawn. Conversely, a service connection may exist while the user does not have permission to receive data from a particular source.
For example, a service provider may operate intelligence that transforms raw sensor data into a prediction. The user may control access to the underlying sensor data, while the service provider retains control over access to the transformation or intelligence they provide. The service provider can therefore terminate access to the service without changing ownership of the user's underlying data source. This creates a separation between who you are, what you own, what data you may receive, what service you may use, and who controls the intelligence applied to that data. That separation is one of the fundamental design principles behind the Real Time Web.

### PAGE
url: https://synx.tools/privacy
title: Privacy Policy - Synx tools

Privacy Policy - Synx tools
Morph Space Who we are Skalle
Privacy
Privacy Policy
Synx AS runs this website. This page explains what we receive when you write to us or join the newsletter, and what we do with it.
Who this covers
Synx tools is the public site for Synx AS. It describes the tools used to configure, secure, and operate a Real Time Web domain: Synx BIOS, Synx DNS, Synx Pass, and Skalle AI. Morph Space is how people and organizations join that network. This policy covers this website, the contact form, and the newsletter.
What you send us
If you use the contact form, we receive the company, name, email address, reason, and message you type. We use that to read your note and reply.
If you join the newsletter, we receive the email address you enter. We use it to send news about Synx. You can ask us to stop, through the contact form.
What we do not do
We do not sell this information. We do not use it for advertising profiles. We do not ask for payment details on this website.
Running the site
The site is hosted so it can be delivered to you. A host may keep short technical logs, such as an address and a time, to keep the service available and to deal with abuse. Those logs are not a marketing list.
How long we keep it
We keep a contact message for as long as we need it to respond and to keep a record of that conversation. We keep a newsletter address until you ask us to remove it, or until we stop sending the newsletter.
Your requests
You can ask what we hold from you, ask us to correct it, or ask us to delete it. Use the contact page. If you are in the European Economic Area, you can also complain to the Norwegian Data Protection Authority, Datatilsynet.
Changes
If this policy changes, the new version will be posted on this page.

### PAGE
url: https://synx.tools/real-time-web-position
title: Real Time Web Position - Synx tools

Real Time Web Position - Synx tools
Morph Space Who we are Skalle
Research
Real Time Web Position
Real Time Web · 4 min read · Dec 2020
Universal building blocks
Real Time Web operates in an emerging competitive market. It means that there are several vendors suggesting a similar problem, in different ways. The position we aim for is: Universal building blocks.
To our knowledge nobody else can offer the same level of versatility or ability to build on each other’s applications.
Our Brand Promise
We let anyone connect anything to the present
Unlike traditional or alternative methods of connecting things and devices to the Web, by means of API and middleware with all its limitations, we let anyone connect anything to the present, through bi-directional linking. This is a whole new innovation game, which enables a shared, user friendly architecture for real time connection of all things, physical and virtual.
Whereas the Web is basically designed to collect, store and transmit linked files in a network, the Real Time Web is intrinsically a network designed to process the virtual and physical present of data. Just like mathematics lacked a concept of zero for a long time, the Web has lacked an elaborate concept of ‘Now’.
The Real Time Web does not store information, but it provides real time data within itself. The data can be accessed, managed and stored through the Web. The Real Time Web can operate as many instances, interconnected with or detached from the Web, on a wide range of carriers.
Brand Proof
Endless digital physical innovation
The reason why we can let anyone connect anything to the present, is that our ecosystem enables endless digital physical innovation.
We present four key features, all reasons to choose and commit to the Real Time Web:
Shared global marketplace
From concepts like App Store and Google Play, we have learned that developers and manufacturers will invest their creativity and resources, where they recognize the most favorable infrastructure and business model. By embedding a billing engine into core web technology, we offer a new global marketplace on a level never seen before, with near infinite potential. We combine the strengths of the open source community, with the incentive of private ownership. Our concern is the vast opportunities it presents to each creator, and the added value they bring into the world. When they can all interact within the same framework and build on each other’s applications, we can hardly imagine the impact as the network effect gains traction.
Security by design
With the increasing omnipresence of information technology and the profound role it plays in society, security is key priority. The foundation of the Real Time Web is developed by security experts with military background and standards. Precautions have been made to resist hacking and surveillance, to respect privacy and ownership, as well as safeguard transactions within the network.
Ultra compatible
Based on common RF specification for wireless sensor networking, and a wide protocol support, the Real Time Web is highly versatile and extremely redundant. The Real Time Web works as the ever expanding intersection between past, present and future applications. The technology is backwards compatible with the Web (WWW, as we know it), and can operate in intranet environments. The link to future applications is particularly innovative, as the ecosystem enables the network to define a need, which encourages others to provide a required data or application. It’s up to every owner to define transaction values in their data or application portfolio. The default value is zero.
Most cost efficient
Our invention bi-directional linking drastically reduces development cost (due to no need for API/middleware). More cost efficiency means less risk, increased innovation rate and even higher profit/margins. We supply the most cost efficient way to develop, maintain and update applications. Across categories, developers and manufacturers are given the means to effortlessly add value and monetize. Because we advocate their rights and ownership to what they create in our ecosystem, they will benefit from a predictable cost and revenue structure nobody else can match.
Brand Concept
Let us make amazing things together!
The story about the Real Time Web is about facilitating creativity through a global network. Our ecosystem fundamentally lowers the technological and economical threshold to innovate. The result is massive business opportunities and real life problem solving.
The driving force behind the Real Time Web will be the increasing demand to connect the physical and virtual world. We address the same kind of creativity that Minecraft has people invest in their virtual worlds. Only in our case, creativity will successively impact the physical world. In our safe environment, making sure everyone gets their share, we encourage people to collaborate, test their ideas, develop applications and work on each other’s accomplishments.
Worth keeping in mind, is that all though the potential and our belief in the Real Time Web is unlimited, its success depend on these simple insights:
The creators must find out we exist and believe that we are the future
Individuals need to realize we represent the biggest potential for them, and why it is true
We enable and develop a platform/an ecosystem, it’s the creativity of our users that generates value
We are excited to see where the creative community of the world will take the Real Time Web. After all, the network will expand through individuals and teams, passionate to make amazing things together.
Back to company posts

### PAGE
url: https://synx.tools/realtimeweb
title: Real Time Web - Synx tools

Real Time Web - Synx tools
Morph Space Who we are Skalle
The Real Time Web
An Internet Designed for a World of Intelligent Machines
The World Wide Web transformed society by making information universally addressable and linkable. But it was fundamentally designed around people requesting information from servers. The next generation of the Internet will have very different users.
AI agents, robots, autonomous vehicles, IoT devices and intelligent services need to continuously discover, access and exchange live data across systems, organizations and physical environments. They need to communicate without requiring a human to initiate every interaction. The Real Time Web (RTW) is a network architecture designed for this machine-driven world.
Instead of treating the Internet primarily as a collection of documents and applications, RTW treats live data, services, machines and intelligence as addressable network resources. Every participating resource can have an identity and address. Data can remain at its source while authorized services subscribe to state changes and receive updates when something actually changes. This creates a fundamentally different model:
From To
requesting information → subscribing to reality
isolated APIs → linkable resources
centralized applications → distributed services
moving data → accessing data at its source
human-driven interaction → autonomous machine communication
A Heterogeneous Network
Real Time Web is not intended to replace the physical Internet. It is an architectural layer that allows different technologies, devices, protocols, data sources and intelligent systems to participate in a common network model.
A temperature sensor, an AI model, a building, a robot, a database or an individual user's data can become part of the same interconnected environment while remaining under different ownership and administrative control. The result is a heterogeneous network where intelligence can be assembled dynamically from resources distributed across the world.
From APIs to Links
Today's digital infrastructure depends heavily on custom integrations. Developers repeatedly connect applications to APIs, databases and cloud services, creating tightly coupled systems that require continuous maintenance. RTW introduces a different principle. Make network resources addressable, then link them.
Once resources can be discovered and addressed consistently, humans and AI can compose services from existing capabilities rather than rebuilding integrations for every application. This becomes particularly important as AI moves from generating information to operating autonomous systems.
Data Remains With Its Owner
A central principle of the Real Time Web is that connectivity should not automatically require surrendering ownership of data. RTW is designed so that data owners can expose controlled channels directly from their own namespace and determine which people, services or machines are permitted to access them. This creates the foundation for user-controlled data sharing, and ultimately for new economic models where data and intelligence can be exchanged directly between producers and consumers.
Synx: Building the Tools
Synx was created to turn the principles of the Real Time Web into technology that developers and machines can actually use. Our tools provide key building blocks for creating and operating RTW services. Synx DNS provides addressing and discovery. Synx BIOS provides the runtime environment. Synx Pass manages identity, ownership and access. Skalle AI helps AI models understand, create and administer Real Time Web services autonomously. Together, these tools allow developers, and increasingly AI itself, to build applications on a network designed for machines.
An Open Invitation to Build the Next Web
We believe the Real Time Web should become larger than any single company. Synx is one implementation of this vision. Developers, researchers, companies and technology communities should be able to explore the architecture, challenge it, extend it and build entirely new products on top of it. Because the next Internet will not be created by one application. It will emerge from everything that becomes connected to it.
Learn more about the architecture, principles and specifications of the Real Time Web at RealTimeWeb.org →

### PAGE
url: https://synx.tools/skalle
title: Skalle AI - Synx tools

Skalle AI - Synx tools
Morph Space Who we are Skalle
Skalle AI
Don't just ask AI to write code. Ask it to build the network.
Skalle AI
AI
Turn intent into infrastructure. An AI interface that helps create, connect, and operate Real Time Web services using your preferred AI model.
From prompt to autonomous service Describe what you want to achieve
AI that builds the network Not just the code
Describe what you need Skalle builds the connection
Skalle is the AI interface to the Real Time Web.
Most AI assistants help you generate text, write code, or interact with existing applications. Skalle is designed for something different: creating and operating distributed services on the Real Time Web.
Skalle has been taught the principles, architecture, and developer tools behind RTW. Through a conversational interface, developers can describe what they want to build and let Skalle help translate that intent into network architecture.
Ask Skalle to create a service, expose a data source, connect existing services, configure access, or suggest how an application should be distributed, and Skalle can use the Synx toolchain to help construct it.
From Conversation to Infrastructure
Imagine telling Skalle: "Create a service that receives live energy data from my buildings, combine it with weather data, give my optimization model access to it, and expose the resulting energy forecast to my application."
Instead of simply explaining how this could be programmed, the goal of Skalle is to help build and configure the actual RTW architecture: describe, discover, create, link, configure, run.
This changes the role of AI from a coding assistant into an infrastructure-building interface.
Bring Your Own Intelligence
Skalle is built around Model Context Protocol (MCP) integration. That means the intelligence does not have to be tied to a single language model. Users can connect compatible AI environments and models while Skalle provides the specialized RTW knowledge and tools required to interact with the network.
Your preferred AI model provides the intelligence. Skalle provides the Real Time Web capabilities.
Native to Morph Space
Skalle will be available directly inside Morph Space, where it becomes a conversational interface to the ecosystem. Instead of manually configuring every component, users can ask Skalle to help create Morph services, connect internal and external data sources, discover existing services, build linking architectures, configure ownership and access, suggest infrastructure for new applications, compose existing data and intelligence into new services, and deploy and administer RTW resources.
As the Morph Space ecosystem grows, Skalle can increasingly help users discover and combine capabilities that already exist rather than rebuilding everything from scratch.
AI That Understands the Network
Traditional AI coding assistants primarily operate around files, codebases, and APIs. Skalle is being designed around a different abstraction: the network itself.
It understands that an application can be assembled from distributed, independently owned resources: data, intelligence, machines, and services, connected through the Real Time Web. That makes Skalle particularly suited to a future where applications are not simply installed or hosted, but dynamically composed from live network resources.
From Prompt to Autonomous Service
The long-term goal is simple. A user should be able to describe what they want to achieve, while Skalle works with the Synx tools and the Real Time Web to determine how to connect the resources required to achieve it.
No single AI model has to own the ecosystem. No single cloud has to own the infrastructure. And the user remains in control of their services and data.
Skalle turns natural language into Real Time Web infrastructure.
FAQ
What is Skalle AI?
Skalle is the AI co-pilot for the Real Time Web. You describe what you want, and Skalle carries out the authorized platform operations and reports the result.
Skalle is the AI co-pilot for the Real Time Web. It allows users to create, configure and operate Synx and Morph Space services simply by describing what they want in natural language. Instead of learning commands, protocols, APIs and administration interfaces, you can tell Skalle what you want to achieve: "Create a service on my domain, add two Ghosts, connect the data source and give Alex read access."
Skalle translates that intent into the required platform operations, executes the authorized actions and reports the result back to you. It can work with domains, Morphic Services, Ghosts, links, access rights, ownership and multi-step workflows. Skalle can be used through its own dashboard, embedded into partner applications, or connected to compatible AI tools through MCP. In simple terms, Skalle makes the Real Time Web as easy to operate as sending a message.
How is Skalle different from a normal AI assistant or coding agent?
Most assistants answer or generate. Skalle is built to operate the Synx and Morph Space platform, inside an isolated session tied to your identity. External AI tools are read-only unless modification is explicitly enabled.
Most AI assistants are designed primarily to answer, explain or generate. Skalle is designed to operate. A general AI assistant might explain how to configure a network service or generate code for an API integration. Skalle can work directly with the Synx/Morph Space platform and perform authorized operations on behalf of the user. This is possible because Skalle is purpose-built around the Real Time Web architecture. It understands its domains, Morphic Services, Ghosts, links, ownership model and access-control mechanisms.
The difference can be summarized simply. A chatbot tells you how. A coding agent helps you build it. Skalle can operate the network. Skalle is also designed with security boundaries around these actions. Each user operates through an isolated AI session associated with their own identity and permissions. External AI tools are read-only by default. Operations that modify the network must be explicitly enabled and can require confirmation before execution, while access tokens automatically expire. This allows AI to become operational without simply giving it unrestricted control of the infrastructure.
Can Skalle create and connect Real Time Web services autonomously?
Yes, within the permissions you grant. Skalle can turn one request into a sequence of network operations. It does not receive rights just because it asks for them.
Yes, within the permissions and controls granted by the user. Skalle can translate a high-level request into a sequence of Real Time Web operations and execute them as a workflow. For example, instead of manually performing several configuration steps, you could ask: "Create an energy service on my domain, add my building as a Ghost, connect it to the weather service and give my optimization service access to the resulting channel."
Skalle can determine the required platform operations and perform the authorized steps in sequence. It can create and update services, manage Ghosts, establish links, configure domains, manage access rights and execute multi-step or batch operations. This makes it possible to move from Prompt, to Plan, to Network Operations, to a Running Service. The objective is not autonomy without control. Skalle operates within the identity, ownership and permissions of the person or organization using it. Actions outside those permissions are not automatically granted simply because an AI requests them. This makes Skalle particularly useful for building autonomous systems: AI can automate the infrastructure while humans retain authority over it.
What is MCP, and can I use Skalle with my preferred AI model?
MCP lets compatible AI applications use the Real Time Web operations Skalle exposes. Your preferred model does the reasoning. Skalle provides the capabilities. It can also run as a Docker service with company SSO.
MCP (Model Context Protocol) provides a standardized way for compatible AI applications to connect to external tools and capabilities. Skalle uses MCP to expose Real Time Web operations to compatible AI environments. This means you do not necessarily have to use a particular language model or AI interface to work with Skalle. You can use Skalle from its own interface or connect compatible AI tools and development environments, including tools such as ChatGPT, Claude, Cursor or VS Code, and let them interact with the capabilities Skalle exposes.
This separation is important to our philosophy. Your preferred AI provides the reasoning. Skalle provides the Real Time Web capabilities. Synx provides the network infrastructure. The result is a model-independent approach that reduces dependency on any single AI vendor. For organizations that require greater control, Skalle can also be deployed as a Docker-based service and integrated with existing company authentication and SSO infrastructure.
What can I ask Skalle to build for me?
You can ask for a single change or a whole workflow: services, Ghosts, links, access, ownership, and a look at what is connected now.
You can ask Skalle to perform individual operations or describe an entire workflow in natural language. For example: "Create a new service on my domain." "Add these three devices as Ghosts." "Show me everything currently connected to this service." "Give this user read access to my data channel." "Transfer ownership of this Ghost." "Connect my service to this external data source." "Show me which Ghosts are waiting for approval." Or you can describe something more complex: "Create a service for my building, connect the temperature and energy data, add an external weather source, and prepare a channel that my AI model can use for energy optimization."
Skalle can break the request into the necessary operations and execute the authorized workflow. It can help you create and update Morphic Services, create, remove and morph Ghosts, establish and manage links, manage domains and their resources, grant and revoke access, transfer ownership, approve ownership requests, perform batch and multi-step operations, inspect active connections and resources, and monitor the current state of your RTW environment.
And because Skalle can be exposed through MCP, these capabilities do not have to remain inside the Skalle interface. They can become tools available to other AI systems. That leads to the larger idea behind Skalle. You shouldn't have to learn how to operate the Real Time Web before you can build on it. Tell AI what you want to create, and let Skalle translate your intent into network operations.

### PAGE
url: https://synx.tools/terms
title: Terms of Use - Synx tools

Terms of Use - Synx tools
Morph Space Who we are Skalle
Terms
Terms of Use
These terms cover your use of this website. They do not set a price for the tools, and they do not replace an agreement for a particular deployment.
The site
This website is published by Synx AS. It explains Synx tools and how they relate to the Real Time Web and Morph Space. Synx DNS names a domain. Synx BIOS operates the layer you own. Synx Pass secures who is connected. Skalle AI helps create, link, and administer services.
Using it
You may read the site and share links to it. Do not misuse it. That includes trying to break the site, interfering with other people, or presenting the material as your own product.
No price list here
Nothing on this website is an offer to sell a plan at a stated price. If a tool or a deployment is made available to you, the terms for that arrangement are agreed separately.
The material
The writing, the Synx name, and the Synx mark on this site belong to Synx AS, unless a page says otherwise. Names such as LinkedIn, X, and Reddit belong to their own owners. A card in the posts section is a preview and a link, not a claim that Synx owns that network.
Information, not a guarantee
We work to keep the site accurate. It is an introduction to the work, not a promise that a feature, a date, or a result will be available to you.
Law
The laws of Norway apply to this website and to these terms.

### PAGE
url: https://synx.tools/tools
title: Our Tools & Services - Synx tools

Our Tools & Services - Synx tools
Morph Space Who we are Skalle
Our Tools & Services
Four tools for a Real Time Web domain
Welcome
A simple place to begin
Synx is the set of tools for a domain you keep. One names it, one runs it, one decides who can use it, and one helps you build the next service. Open any card below and start there.
Synx BIOS
The command line for the layer you own. Administer services, share or transfer a data source, and see what belongs to you.
Synx DNS
Client DNS for the domain. Map an address to a root domain, subdomains, and Morphic services. Set data links, and change the structure when the service needs to.
Synx Pass
Identity, authentication, and ownership. People, services, and machines are recognized here. Access follows the owner, and it can move when ownership moves.
Skalle AI
Turn intent into infrastructure. An AI interface that helps create, connect, and operate Real Time Web services using your preferred AI model.
Morph Space
DNS names the domain. BIOS operates it. Pass secures who is connected. Skalle helps create, link, and administer the services. The same network, whichever layer you own.
Four tools One network
Use the tool that matches the layer you own. The suite is how a domain is named, secured, operated, and built.
Synx DNS Names the domain, the services, and the links.
Synx BIOS Operates the layer you own.
Synx Pass Secures who is connected, and what they own.
Skalle AI Helps create, link, and administer services.

### PAGE
url: https://synx.tools/who
title: Who we are - Synx tools

Who we are - Synx tools
Morph Space Who we are Skalle
Who we are
India
Company history
It Started With a Question
What if the Web could connect more than information? The story behind Synx began in 2008 with a question that seemed simple at the time: what would the Web look like if it had been designed for machines as well as humans?
I had spent much of my career working with computers, mobile technology and distributed systems. I had watched the Internet transform from something used by specialists into infrastructure that changed almost every part of society. And yet something about its architecture kept bothering me.
The World Wide Web was brilliant at connecting information. A document could link to another document anywhere in the world. Anyone could publish, anyone could browse, and the network could grow without anyone controlling the whole thing. But machines were different.
A machine doesn't need to read a webpage about the temperature. It needs to know that the temperature just changed. A robot doesn't want to repeatedly ask a server whether something has happened. It needs the relevant change delivered when it happens. And intelligent systems shouldn't require developers to manually integrate every sensor, database, application and service they encounter.
The Web had given us a universal way to link information. We started wondering whether the same fundamental idea could be applied to live data and intelligence.
From an Idea to an Architecture
In 2008, Henrik Silverkant and I began exploring this problem seriously. We were inspired by the simplicity and openness of Sir Tim Berners-Lee's World Wide Web, but also by ideas about interconnected systems and collective behaviour. Instead of asking how we could improve the existing Web, we started from a different question: how would we design a network if autonomous machines were its users?
That question eventually led to an architecture we called Morphic Architecture Design, MAD. The idea was to make network resources directly addressable and allow them to form bidirectional relationships across domains.
Rather than continuously moving copies of data between applications, data could remain associated with its source. Services could subscribe to changes. Different systems could transform, or morph, data into the structures required by the next participant in the network. The network would no longer simply connect computers. It could connect things, data, services and intelligence. That became the foundation of what we now call the Real Time Web.
Years Before the AI Revolution
At the time, this was a difficult idea to explain. AI agents were not part of everyday conversation. Humanoid robots were mostly research projects. IoT was still emerging. Cloud computing itself was relatively young. We were developing infrastructure for a world that had not arrived yet.
So we spent years experimenting. We connected sensors and devices. We worked with different communication technologies. We built demonstrations and proof-of-concepts. We tested the architecture in real environments and learned where it worked, and where it didn't. The technology evolved through every project.
What originally looked like an architecture for connecting devices gradually revealed something much larger. If software services could be addressed and linked dynamically, then intelligence itself could become part of the network. One intelligent service could consume another. Multiple services could collaborate. Data could move through chains of transformation before reaching a person, application or machine. Long before today's explosion of AI agents, we were working toward networks of cooperating intelligence.
Then the World Caught Up
The arrival of modern AI changed the context completely. Suddenly, machines could understand instructions, reason about information, generate software and interact with external tools. But the underlying infrastructure remained largely the same.
Today's AI is extraordinarily capable inside a model, but connecting that intelligence reliably to the physical and digital world still requires APIs, integrations, databases, cloud platforms and substantial engineering. To us, this looked familiar. It was the problem we had been working on for years. The missing piece was no longer intelligence.
The Real Time Web
That realization brought us back to the original vision with renewed urgency. The Real Time Web is our answer. It is not intended to replace the Internet or the World Wide Web. It extends the idea of the Web into a world where the participants increasingly include AI agents, sensors, robots, autonomous systems and intelligent services.
Where the traditional Web made documents addressable and linkable, RTW aims to make live network resources addressable and linkable. Where today's applications repeatedly request information, RTW is designed around changes in state. Where conventional integrations move and duplicate data, RTW is designed to let authorized consumers connect closer to the source. And where today's AI systems often operate as isolated services, RTW provides an architecture for connecting intelligence across independently owned domains. The vision is simple:
Synx Is Born
Eventually we realized that an architecture alone would never create a new Web. Developers needed tools. The original World Wide Web became transformative because people could create websites, register domains, run servers and link their work to everybody else's. The Real Time Web needs the same thing.
That is why we created Synx. Synx turns the concepts developed through years of RTW research into practical developer technology. Synx DNS gives network resources identity, addressing and discovery. Synx BIOS provides the runtime environment for creating and operating Real Time Web services. Synx Pass provides identity, ownership and controlled access. And Skalle AI introduces something we could only imagine when this journey started: an AI interface capable of understanding the Real Time Web and helping humans and other AI models create, link and administer RTW services.
A developer can increasingly describe what they want to create rather than manually configuring every connection. In a strange way, AI may ultimately become one of the most important developers of the network we originally designed for AI.
From Synx to Morph Space
The next step is Morph Space . If Synx provides the tools for creating the network, Morph Space is where the network can become an economy.
People, organizations and machines continuously produce data. RTW makes it possible to address those resources at their source and organize them into controlled channels. Morph Space is being developed so those channels, and the intelligence that transforms them, can be discovered, linked and ultimately traded.
A sensor can contribute data. An AI service can add intelligence. Another service can transform it. A robot, application or person can consume the result. Each participant can potentially contribute to the value chain while the source owner maintains control over access to the underlying resource.
Real Time Web makes data linkable. Morph Space makes it tradable.
2008 Was Only the Beginning
When Henrik and I began this journey, we could not have predicted today's world of language models, autonomous AI agents and increasingly capable robots. But the question that started everything has become more relevant, not less: what network will all these intelligent machines use?
Our answer has taken years of research, experimentation, successes, failures and rebuilding. Today, Synx represents the next chapter. We are no longer only researching what the next Web could look like. We are building the tools that allow others to build it with us. And this time, some of those builders won't be human.
- By Paal Kristian Levang
The Story Continues
The Real Time Web is bigger than one company or one product. It is an architectural concept for connecting live data, services, machines and intelligence across independently controlled domains. Synx exists to turn that concept into usable technology.
Explore the architecture, principles and vision behind the Real Time Web at RealTimeWeb.org .
Meet the Crew
Humans, engineers, creators, and one AI.
Building the Real Time Web one connection at a time.
The Founders / Bridge Crew
Paal, The Architect
Inventor of worlds. Breaker of protocols.
LinkedIn
Connect with Paal
Open their profile and say hello.
View profile
Ken, The Captain
Keeping the ship, crew and mission on course.
LinkedIn
Connect with Ken
Open their profile and say hello.
View profile
Henrik, The Tech Hero
When technology fights back, send Henrik.
LinkedIn
Connect with Henrik
Open their profile and say hello.
View profile
The Lab
Shrey, The AI Alchemist
Turning data, models and algorithms into intelligence.
LinkedIn
Connect with Shrey
Open their profile and say hello.
View profile
Yash, The Full-Stack Jedi
From interface to infrastructure, the stack is strong with this one.
LinkedIn
Connect with Yash
Open their profile and say hello.
View profile
Asveig, The Visual Storyteller
Turning complex technology into something humans actually understand.
The Engine Room
Vijay, The Code Keeper
Guardian of repositories, builds and the sacred source.
LinkedIn
Connect with Vijay
Open their profile and say hello.
View profile
Thiru, The Swiss Army Engineer
If it needs building, fixing or figuring out, call Thiru.
LinkedIn
Connect with Thiru
Open their profile and say hello.
View profile
Skalle, The Morph Master
Not human. Still invited to every team meeting.
Company core values
Reciprocity
We depend on each other and the world around us. What we give, somehow comes back to us. By responding to positive actions, with positive actions, we create a friendly atmosphere around ourselves and what we do. This is a universal social principle, inherent in our company as well as in our technology.
Simplicity
Because we are engaged in complex matters, we recognise simplification to be fundamental. Through simplicity we make things possible, accessible and valuable.
Community
Both in our company and in general, we grow through our ability to cooperate and work as a team. Being adherents of the global open source community, we share our ideas and build upon each other.
Join Discord
The work
Use the tools, or write to us.
The suite is on this site. If you want to build with Synx, or talk to the company, start there.
Let's build what comes next
We believe the next generation of the Internet will be shaped by people and machines working together, and it will take more than one company to build it. Whether you are an investor, industry partner, inventor, developer, researcher, journalist, or simply curious about what we are creating, we would love to hear from you.
We are always open to new ideas, unexpected collaborations and partnerships that can help turn autonomous technology into something useful for people, society and the planet. If you see an opportunity to build something meaningful together, let's talk.
Reason Commercial Industrial partners Investors Technical Support Media Inventors and creators of the new earth
Company Name Email Message Send
Early access
Enter your email for early access to the newsletter.
Email address Join

### PAGE
url: https://synx.tools/
title: Synx tools

Synx tools
Morph Space Who we are Skalle
Run it live Keep it yours
Synx is the tool suite for domain owners, developers, and consumers. It configures, secures, and operates the network, while each role keeps the layer that belongs to them.
Company posts
Signals from Synx
From the people building Synx. The tools, the work, and the partnerships taking the Real Time Web from an idea into a network.
Paal Kristian Levang Synx Editorial Articles Are we raising the world’s first superintelligence to be a narcissist?
Humanity may be facing its greatest experiment ever. We are in the process of developing an intelligence that could be smarter than ourselves.
Read Oct 2026 Thiru Medium Articles Are We Just Another Training Dataset for the Future?
Recently, I started watching a show on Netflix called Black Mirror. It is genuinely scary, but it also reflects the truth about humanity.
Read Oct 2026 Paal Kristian Levang LinkedIn Articles The Last IT Project
The new network is called Real Time Web (RTW) and is a bidirectional Linked Data network with inbuilt network kernel (BIOS) access, so that individuals can have full control over their Web resources and services globally.
Visit Jan 2018
Thiru Synx Articles Friend or foe? The choice is still ours
We keep hearing that AI is going to take the jobs. The other side is harder to ignore: the same tools are helping people reach work, company, and worlds they could not reach alone.
Read Oct 2026 Real Time Web LinkedIn Partnership
The Real Time Web Seed Round is now open. We are raising $6 million to launch what we believe is the next generation of internet infrastructure for AI agents, autonomous machines, and real-time data.
Visit 2mo Thiru LinkedIn Research
What if machines didn't need servers to talk to each other? Today, the internet mostly looks like: You → App → API → Server → Database → You
Visit 5d Paal Kristian Levang LinkedIn Launch
Finally!, We've closed our pre-seed round and are moving toward launch in August! After years of R&D, we're finally releasing what we've been building:
Visit 4mo
Real Time Web Journal Research Real Time Web Position
Real Time Web operates in an emerging competitive market. It means that there are several vendors suggesting a similar problem, in different ways. The position we aim for is: Universal building blocks.
Read Dec 2020 Paal Kristian Levang Journal Articles Internet for machines
A new kind of internet is coming: one that doesn't just connect websites, but gives intelligence to the objects all around us.
Read Sep 2026 Thiru LinkedIn Field notes
The Internet was never really built for machines. And it shows. Every time your smartwatch talks to an app, your Tesla talks to a server, or your smart thermostat learns your habits, that data usually does not stay with you.
Visit 1w
Paal Kristian Levang Journal Articles Autonomous machine networks
The Real-Time Web (RTW), also known as the AI Web, represents a fundamental shift in how the world's machines, robots, AI agents, and even humans connect to digital intelligence.
Read Sep 2026 Thiru LinkedIn Articles
Been sitting on something for the last few weeks that's genuinely changed how I think about the internet. We've built the web around linking documents. Click a link, get a page.
Visit 2d Paal Kristian Levang LinkedIn Launch
The countdown has begun. Morph Space is almost here. We're not just launching another platform.
Visit 2mo
