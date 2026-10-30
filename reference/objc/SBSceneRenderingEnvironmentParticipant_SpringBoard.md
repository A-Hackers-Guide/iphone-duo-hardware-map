# `SBSceneRenderingEnvironmentParticipant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 2 instance variables, 6 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSString" _renderingEnvironmentIdentifier;
@"<BSInvalidatable>" _assertion;
```

## Properties

```
@property (T@"<BSInvalidatable>",R,N,V_assertion) assertion;
@property (T@"NSString",R,C,N,V_renderingEnvironmentIdentifier) renderingEnvironmentIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneRenderingEnvironmentParticipant assertion];
-[SBSceneRenderingEnvironmentParticipant invalidate];
-[SBSceneRenderingEnvironmentParticipant initWithRenderingEnvironmentIdentifier:assertion:];
-[SBSceneRenderingEnvironmentParticipant renderingEnvironmentIdentifier];
```
