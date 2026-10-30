# `SBAssistantIslandStageKeyboardPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBScenePresenting`, `BSDescriptionStreaming`, `BSInvalidatable`
- 4 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<SBAssistantIslandStageKeyboardPresenterDelegate>" _delegate;
@"<BSInvalidatable>" _inputUIPresenterAssertion;
@"<SBScenePresentingDelegate>" _inputUIPresentingDelegate;
@"UIView" _inputUIWrapperView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAssistantIslandStageKeyboardPresenter setPresentingDelegate:];
-[SBAssistantIslandStageKeyboardPresenter dismissScene:];
-[SBAssistantIslandStageKeyboardPresenter initWithDelegate:];
-[SBAssistantIslandStageKeyboardPresenter debugDescription];
-[SBAssistantIslandStageKeyboardPresenter init];
-[SBAssistantIslandStageKeyboardPresenter dealloc];
-[SBAssistantIslandStageKeyboardPresenter presentScene:viewControllerBuilderBlock:];
-[SBAssistantIslandStageKeyboardPresenter succinctDescription];
-[SBAssistantIslandStageKeyboardPresenter invalidate];
-[SBAssistantIslandStageKeyboardPresenter description];
-[SBAssistantIslandStageKeyboardPresenter appendDescriptionToStream:];
-[SBAssistantIslandStageKeyboardPresenter isEligible];
-[SBAssistantIslandStageKeyboardPresenter _updateKeyboardRenderId:contextId:];
-[SBAssistantIslandStageKeyboardPresenter assistantIslandScene];
-[SBAssistantIslandStageKeyboardPresenter currentDisplayIdentity];
-[SBAssistantIslandStageKeyboardPresenter isVisibleOnScreen];
-[SBAssistantIslandStageKeyboardPresenter noteVisibilityMayHaveChanged];
-[SBAssistantIslandStageKeyboardPresenter parentSceneIdentityToken];
```
