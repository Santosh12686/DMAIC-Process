# Process Map — Current vs Future

## Current state (black-hole gap)

```mermaid
flowchart LR
  A[Customer lodges dispute] --> B[Case created]
  B --> C[Docs collected]
  C --> D[Back-end investigation]
  D --> E[Decision recorded]
  E --> F[Manual / delayed notify]
  D -.->|No customer-visible updates| X[Customer phones for status]
  X --> Y[Agent looks up case]
  Y --> D
```

The dashed path is the **communication black hole**: investigation progresses internally while customer channels stay silent.

## Future state (event-driven)

```mermaid
flowchart LR
  A[Customer lodges dispute] --> B[Case created]
  B --> N1[Notify: received]
  B --> C[Docs collected]
  C --> N2[Notify: docs received / info needed]
  C --> D[Under review]
  D --> N3[Notify: under review]
  D --> E[Decision]
  E --> N4[Notify: finalized]
  N1 & N2 & N3 & N4 --> Ch[App / SMS / secure message]
```

## Key finding
Customers do not primarily chase because the process is slow; they chase because they lack **real-time status updates**.
