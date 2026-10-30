# `MTLDepthStencilStateSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLDepthStencilState`
- 0 instance variables, 6 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R) readsDepth;
@property (TB,R) writesDepth;
@property (TB,R) readsStencil;
@property (TB,R) writesStencil;
@property (TQ,R) uniqueIdentifier;
@property (TQ,R,N) resourceIndex;
```

## Instance methods

```
-[MTLDepthStencilStateSPI resourceIndex];
-[MTLDepthStencilStateSPI uniqueIdentifier];
-[MTLDepthStencilStateSPI readsDepth];
-[MTLDepthStencilStateSPI readsStencil];
-[MTLDepthStencilStateSPI writesDepth];
-[MTLDepthStencilStateSPI writesStencil];
```
