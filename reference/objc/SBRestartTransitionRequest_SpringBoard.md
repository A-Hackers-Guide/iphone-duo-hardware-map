# `SBRestartTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 7 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _requester;
@"NSString" _reason;
i _restartType;
d _delay;
B _wantsPersistentSnapshot;
@"NSArray" _customOverlayDescriptors;
@"NSURL" _applicationLaunchURL;
```

## Properties

```
@property (T@"NSString",C,N,V_requester) requester;
@property (T@"NSString",C,N,V_reason) reason;
@property (Ti,N,V_restartType) restartType;
@property (Td,N,V_delay) delay;
@property (TB,N,V_wantsPersistentSnapshot) wantsPersistentSnapshot;
@property (T@"NSArray",C,N,V_customOverlayDescriptors) customOverlayDescriptors;
@property (T@"NSURL",C,N,V_applicationLaunchURL) applicationLaunchURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRestartTransitionRequest succinctDescriptionBuilder];
-[SBRestartTransitionRequest init];
-[SBRestartTransitionRequest setReason:];
-[SBRestartTransitionRequest descriptionWithMultilinePrefix:];
-[SBRestartTransitionRequest requester];
-[SBRestartTransitionRequest succinctDescription];
-[SBRestartTransitionRequest delay];
-[SBRestartTransitionRequest setDelay:];
-[SBRestartTransitionRequest description];
-[SBRestartTransitionRequest reason];
-[SBRestartTransitionRequest copyWithZone:];
-[SBRestartTransitionRequest setRequester:];
-[SBRestartTransitionRequest descriptionBuilderWithMultilinePrefix:];
-[SBRestartTransitionRequest applicationLaunchURL];
-[SBRestartTransitionRequest setRestartType:];
-[SBRestartTransitionRequest customOverlayDescriptors];
-[SBRestartTransitionRequest initWithRequester:reason:];
-[SBRestartTransitionRequest restartType];
-[SBRestartTransitionRequest setApplicationLaunchURL:];
-[SBRestartTransitionRequest setCustomOverlayDescriptors:];
-[SBRestartTransitionRequest setWantsPersistentSnapshot:];
-[SBRestartTransitionRequest wantsPersistentSnapshot];
```
