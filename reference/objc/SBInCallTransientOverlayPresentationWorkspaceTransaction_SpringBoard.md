# `SBInCallTransientOverlayPresentationWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _analyticsSource;
@"SBInCallPresentationSession" _sourcePresentationSession;
```

## Properties

```
@property (T@"NSString",R,C,N,V_analyticsSource) analyticsSource;
@property (T@"SBInCallPresentationSession",R,N,V_sourcePresentationSession) sourcePresentationSession;
```

## Instance methods

```
-[SBInCallTransientOverlayPresentationWorkspaceTransaction _begin];
-[SBInCallTransientOverlayPresentationWorkspaceTransaction analyticsSource];
-[SBInCallTransientOverlayPresentationWorkspaceTransaction _performInCallPresentationWithCompletion:];
-[SBInCallTransientOverlayPresentationWorkspaceTransaction initWithTransitionRequest:sourcePresentationSession:analyticsSource:];
-[SBInCallTransientOverlayPresentationWorkspaceTransaction sourcePresentationSession];
```
