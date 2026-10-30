# `SBCompanionSceneRestrictor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSInvalidatable`
- 5 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBCompanionSceneRestrictionCoordinator" _coordinator;
@"NSHashTable" _observers;
@"BSCompoundAssertion" _compoundAssertion;
@"NSString" _presentationMode;
@"NSSet" _possibleRestrictions;
```

## Properties

```
@property (T@"NSString",R,C,N,V_presentationMode) presentationMode;
@property (T@"NSSet",R,C,N,V_possibleRestrictions) possibleRestrictions;
@property (T@"NSString",R,C,N) currentRestriction;
@property (TB,R,N) isRestricted;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCompanionSceneRestrictor isRestricted];
-[SBCompanionSceneRestrictor presentationMode];
-[SBCompanionSceneRestrictor removeObserver:];
-[SBCompanionSceneRestrictor dealloc];
-[SBCompanionSceneRestrictor addObserver:];
-[SBCompanionSceneRestrictor invalidate];
-[SBCompanionSceneRestrictor appendDescriptionToStream:];
-[SBCompanionSceneRestrictor _allOrderedRestrictions];
-[SBCompanionSceneRestrictor _notifyObserversOfRestrictionUpdate:];
-[SBCompanionSceneRestrictor acquireAssertionForPresentationRestriction:];
-[SBCompanionSceneRestrictor currentRestriction];
-[SBCompanionSceneRestrictor initWithCoordinator:presentationMode:possibleRestrictions:];
-[SBCompanionSceneRestrictor possibleRestrictions];
```
