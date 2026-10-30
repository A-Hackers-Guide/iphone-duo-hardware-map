# `MTLResidencySetSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResidencySet`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",?,R,C) allCommittedAllocations;
@property (TQ,?,N) currentGeneration;
@property (TQ,?,N) expiredGeneration;
```

## Instance methods

```
-[MTLResidencySetSPI setCurrentGeneration:];
-[MTLResidencySetSPI currentGeneration];
-[MTLResidencySetSPI allCommittedAllocations];
-[MTLResidencySetSPI expiredGeneration];
-[MTLResidencySetSPI generationForAllocation:];
-[MTLResidencySetSPI setExpiredGeneration:];
```
