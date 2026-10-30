# `SBDisplayBlankingRegionElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAElementViewProviding`, `SBSystemApertureElementAssertionObserving`, `SBSystemApertureElement`, `SBSystemApertureElementVisibilityObserving`
- 6 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSString" _regionIdentifier;
@"SBWindowScene" _windowScene;
i _appearState;
B _teardownDelivered;
@"NSString" _elementIdentifier;
@"<SBDisplayBlankingRegionElementDelegate>" _delegate;
```

## Properties

```
@property (T@"NSString",R,C,N,V_regionIdentifier) regionIdentifier;
@property (T@"<SBDisplayBlankingRegionElementDelegate>",W,N,V_delegate) delegate;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N,V_elementIdentifier) elementIdentifier;
```

## Instance methods

```
-[SBDisplayBlankingRegionElement clientIdentifier];
-[SBDisplayBlankingRegionElement systemApertureElementAssertionInvalidated];
-[SBDisplayBlankingRegionElement element];
-[SBDisplayBlankingRegionElement elementIdentifier];
-[SBDisplayBlankingRegionElement element:visibilityDidChange:];
-[SBDisplayBlankingRegionElement systemApertureElementAssertionAcquired];
-[SBDisplayBlankingRegionElement viewProvider];
-[SBDisplayBlankingRegionElement dealloc];
-[SBDisplayBlankingRegionElement _canShowWhileLocked];
-[SBDisplayBlankingRegionElement setDelegate:];
-[SBDisplayBlankingRegionElement element:visibilityWillChange:];
-[SBDisplayBlankingRegionElement delegate];
-[SBDisplayBlankingRegionElement appearState];
-[SBDisplayBlankingRegionElement destinationWindowScene];
-[SBDisplayBlankingRegionElement regionIdentifier];
-[SBDisplayBlankingRegionElement _deliverDisappearanceCanceled:];
-[SBDisplayBlankingRegionElement hasBlankingRegionBehavior];
-[SBDisplayBlankingRegionElement initWithBlankingRegionIdentifier:windowScene:];
```
