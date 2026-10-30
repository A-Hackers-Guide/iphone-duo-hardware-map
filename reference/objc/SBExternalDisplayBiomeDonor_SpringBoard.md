# `SBExternalDisplayBiomeDonor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSExternalDisplayServiceObserver`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBSExternalDisplayService" _externalDisplayService;
@"NSMutableDictionary" _biomeDonationTimers;
```

## Properties

```
@property (T@"SBSExternalDisplayService",R,N,V_externalDisplayService) externalDisplayService;
@property (T@"NSMutableDictionary",&,N,V_biomeDonationTimers) biomeDonationTimers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBExternalDisplayBiomeDonor init];
-[SBExternalDisplayBiomeDonor dealloc];
-[SBExternalDisplayBiomeDonor externalDisplayWillDisconnect:];
-[SBExternalDisplayBiomeDonor externalDisplayDidConnect:];
-[SBExternalDisplayBiomeDonor externalDisplayService];
-[SBExternalDisplayBiomeDonor _donateToBiomeIfNecessaryForDisplayInfo:connect:];
-[SBExternalDisplayBiomeDonor biomeDonationTimers];
-[SBExternalDisplayBiomeDonor setBiomeDonationTimers:];
```
