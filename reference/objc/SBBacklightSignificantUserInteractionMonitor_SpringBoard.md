# `SBBacklightSignificantUserInteractionMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalEventHandling`
- 2 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"CSCoverSheetViewController" _coverSheetViewController;
```

## Properties

```
@property (T@"CSCoverSheetViewController",W,N,V_coverSheetViewController) coverSheetViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBBacklightSignificantUserInteractionMonitor coverSheetViewController];
-[SBBacklightSignificantUserInteractionMonitor handleEvent:];
-[SBBacklightSignificantUserInteractionMonitor wouldHandleButtonEvent:];
-[SBBacklightSignificantUserInteractionMonitor removeObserver:];
-[SBBacklightSignificantUserInteractionMonitor addObserver:];
-[SBBacklightSignificantUserInteractionMonitor setCoverSheetViewController:];
-[SBBacklightSignificantUserInteractionMonitor conformsToCSEventHandling];
-[SBBacklightSignificantUserInteractionMonitor coverSheetIdentifier];
-[SBBacklightSignificantUserInteractionMonitor participantState];
-[SBBacklightSignificantUserInteractionMonitor _notifyObserversOfSignificantUserInteraction];
```
