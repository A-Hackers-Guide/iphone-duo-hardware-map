# `MTLResourceSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResource`
- 0 instance variables, 4 properties, 12 instance methods, 0 class methods

## Properties

```
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
```

## Instance methods

```
-[MTLResourceSPI isComplete];
-[MTLResourceSPI unfilteredResourceOptions];
-[MTLResourceSPI protectionOptions];
-[MTLResourceSPI waitUntilComplete];
-[MTLResourceSPI isPurgeable];
-[MTLResourceSPI setResponsibleProcess:];
-[MTLResourceSPI allocationID];
-[MTLResourceSPI doesAliasAllResources:count:];
-[MTLResourceSPI doesAliasAnyResources:count:];
-[MTLResourceSPI doesAliasResource:];
-[MTLResourceSPI responsibleProcess];
-[MTLResourceSPI setOwnerWithIdentity:];
```
