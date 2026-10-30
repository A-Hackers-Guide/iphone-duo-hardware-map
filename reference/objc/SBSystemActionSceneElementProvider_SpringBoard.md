# `SBSystemActionSceneElementProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureSceneElementPlaceholderContentProviding`, `SBUISystemApertureContentViewContaining`
- 11 instance variables, 12 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemApertureBackgroundActivitiesSuppressing><SAElementRegistering>" _backgroundSuppressingElementRegistrar;
@"<SBUISystemApertureContentViewProviding>" _leadingPlaceholderContentViewProvider;
@"<SBUISystemApertureContentViewProviding>" _trailingPlaceholderContentViewProvider;
@"<SBSystemActionPreviewContextProviding>" _previewContext;
@"<SAElementIdentifying>" _elementIdentification;
@"<SAInvalidatable>" _elementAssertion;
@"UIColor" _keyColor;
@"UIView" _leadingView;
@"UIView" _trailingView;
@"SBSystemAction" _systemAction;
@"SBSystemApertureSceneElement" _sceneElement;
```

## Properties

```
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (Tq,R,N) contentRole;
@property (TQ,R,N) presentationBehaviors;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemActionSceneElementProvider presentationBehaviors];
-[SBSystemActionSceneElementProvider keyColor];
-[SBSystemActionSceneElementProvider minimalView];
-[SBSystemActionSceneElementProvider contentRole];
-[SBSystemActionSceneElementProvider trailingView];
-[SBSystemActionSceneElementProvider leadingView];
-[SBSystemActionSceneElementProvider clientIdentifier];
-[SBSystemActionSceneElementProvider elementIdentifier];
-[SBSystemActionSceneElementProvider preferredContentSizeDidInvalidateForContentViewProvider:];
-[SBSystemActionSceneElementProvider noteSceneClientWantsControlOfElementWithAssertionTransferBlock:];
```
