# `SBCoverSheetBiometricResourceObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIBiometricResourceObserver`, `SBPearlMatchingStateProvider`
- 3 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _seenMatchResultSinceScreenOn;
@"<SBPearlMatchingStateProviderDelegate>" _delegate;
@"<SBUIBiometricResource>" _biometricResource;
```

## Properties

```
@property (TB,N,V_seenMatchResultSinceScreenOn) seenMatchResultSinceScreenOn;
@property (T@"<SBUIBiometricResource>",W,N,V_biometricResource) biometricResource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBPearlMatchingStateProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) pearlMatchEnabledAndPossible;
```

## Instance methods

```
-[SBCoverSheetBiometricResourceObserver biometricResource];
-[SBCoverSheetBiometricResourceObserver reset];
-[SBCoverSheetBiometricResourceObserver setDelegate:];
-[SBCoverSheetBiometricResourceObserver setBiometricResource:];
-[SBCoverSheetBiometricResourceObserver delegate];
-[SBCoverSheetBiometricResourceObserver biometricResource:observeEvent:];
-[SBCoverSheetBiometricResourceObserver initWithBiometricResource:];
-[SBCoverSheetBiometricResourceObserver pearlMatchEnabledAndPossible];
-[SBCoverSheetBiometricResourceObserver seenMatchResultSinceScreenOn];
-[SBCoverSheetBiometricResourceObserver setSeenMatchResultSinceScreenOn:];
```
