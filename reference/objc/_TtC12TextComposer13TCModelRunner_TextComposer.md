# `_TtC12TextComposer13TCModelRunner`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCModelRunnerProtocol`
- 3 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
_$sSDySuScTyyt Swift.Never requestIdToTask;
_$sShySuG tasksPendingCancellation;
DispatchQueue cancellationQueue;
```

## Instance methods

```
-[_TtC12TextComposer13TCModelRunner init];
-[_TtC12TextComposer13TCModelRunner requestPrewarmingFor:pid:appPid:preferredLanguage:regionPolicy:];
-[_TtC12TextComposer13TCModelRunner computeBasicSmartRepliesWith:conversation:lastMessage:pid:appPid:userPreferredLanguage:shouldSuppressValidation:isPrecomputeRequest:completionHandler:];
-[_TtC12TextComposer13TCModelRunner computePersonalizedSmartRepliesWith:conversation:lastMessage:userProfile:pid:appPid:userPreferredLanguage:shouldSuppressValidation:isPrecomputeRequest:completionHandler:];
-[_TtC12TextComposer13TCModelRunner isAvailableWith:];
-[_TtC12TextComposer13TCModelRunner requestCancellationFor:];
-[_TtC12TextComposer13TCModelRunner requestModelInvocationForQuestionnaireWith:prompt:modelType:pid:requestIdentifier:regionPolicy:completionHandler:];
-[_TtC12TextComposer13TCModelRunner requestModelInvocationWith:prompt:modelType:isPrecomputeRequest:seed:draftSteps:pid:appPid:requestIdentifier:regionPolicy:disallowedStrings:priorInferenceOutput:completionHandler:];
```
