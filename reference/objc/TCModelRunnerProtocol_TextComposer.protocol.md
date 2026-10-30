# `TCModelRunnerProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance methods

```
-[TCModelRunnerProtocol requestPrewarmingFor:pid:appPid:preferredLanguage:regionPolicy:];
-[TCModelRunnerProtocol computeBasicSmartRepliesWith:conversation:lastMessage:pid:appPid:userPreferredLanguage:shouldSuppressValidation:isPrecomputeRequest:completionHandler:];
-[TCModelRunnerProtocol computePersonalizedSmartRepliesWith:conversation:lastMessage:userProfile:pid:appPid:userPreferredLanguage:shouldSuppressValidation:isPrecomputeRequest:completionHandler:];
-[TCModelRunnerProtocol isAvailableWith:];
-[TCModelRunnerProtocol requestCancellationFor:];
-[TCModelRunnerProtocol requestModelInvocationForQuestionnaireWith:prompt:modelType:pid:requestIdentifier:regionPolicy:completionHandler:];
-[TCModelRunnerProtocol requestModelInvocationWith:prompt:modelType:isPrecomputeRequest:seed:draftSteps:pid:appPid:requestIdentifier:regionPolicy:disallowedStrings:priorInferenceOutput:completionHandler:];
```
