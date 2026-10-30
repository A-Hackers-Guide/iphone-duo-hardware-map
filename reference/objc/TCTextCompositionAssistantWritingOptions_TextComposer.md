# `TCTextCompositionAssistantWritingOptions`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 18 instance variables, 18 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _smartQuotesEnabled;
B _smartDashesEnabled;
B _suppressValidation;
B _automaticallyInvoked;
Q _token;
Q _processIdentifier;
Q _appProcessIdentifier;
@"NSString" _requestIdentifier;
@"NSString" _bundleIdentifier;
@"NSString" _rewritingType;
@"NSString" _userPreferredLanguage;
@"NSArray" _userPreferredLanguages;
@"NSArray" _userQuotesArray;
Q _seed;
Q _draftSteps;
Q _regionPolicy;
Q _outputFormatOptions;
Q _maximumReflectionIterationCount;
```

## Properties

```
@property (TQ,R,V_token) token;
@property (TQ,R,V_processIdentifier) processIdentifier;
@property (TQ,R,V_appProcessIdentifier) appProcessIdentifier;
@property (T@"NSString",R,C,V_requestIdentifier) requestIdentifier;
@property (T@"NSString",R,C,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,V_rewritingType) rewritingType;
@property (T@"NSString",R,C,V_userPreferredLanguage) userPreferredLanguage;
@property (T@"NSArray",R,C,V_userPreferredLanguages) userPreferredLanguages;
@property (TB,R,V_smartQuotesEnabled) smartQuotesEnabled;
@property (TB,R,V_smartDashesEnabled) smartDashesEnabled;
@property (T@"NSArray",R,C,V_userQuotesArray) userQuotesArray;
@property (TQ,R,V_seed) seed;
@property (TQ,R,V_draftSteps) draftSteps;
@property (TQ,R,V_outputFormatOptions) outputFormatOptions;
@property (TQ,R,V_regionPolicy) regionPolicy;
@property (TB,R,V_suppressValidation) suppressValidation;
@property (TB,R,V_automaticallyInvoked) automaticallyInvoked;
@property (TQ,V_maximumReflectionIterationCount) maximumReflectionIterationCount;
```

## Instance methods

```
-[TCTextCompositionAssistantWritingOptions seed];
-[TCTextCompositionAssistantWritingOptions smartQuotesEnabled];
-[TCTextCompositionAssistantWritingOptions requestIdentifier];
-[TCTextCompositionAssistantWritingOptions bundleIdentifier];
-[TCTextCompositionAssistantWritingOptions initWithOptions:];
-[TCTextCompositionAssistantWritingOptions smartDashesEnabled];
-[TCTextCompositionAssistantWritingOptions description];
-[TCTextCompositionAssistantWritingOptions token];
-[TCTextCompositionAssistantWritingOptions processIdentifier];
-[TCTextCompositionAssistantWritingOptions copyWithZone:];
-[TCTextCompositionAssistantWritingOptions draftSteps];
-[TCTextCompositionAssistantWritingOptions regionPolicy];
-[TCTextCompositionAssistantWritingOptions maximumReflectionIterationCount];
-[TCTextCompositionAssistantWritingOptions userQuotesArray];
-[TCTextCompositionAssistantWritingOptions appProcessIdentifier];
-[TCTextCompositionAssistantWritingOptions automaticallyInvoked];
-[TCTextCompositionAssistantWritingOptions outputFormatOptions];
-[TCTextCompositionAssistantWritingOptions rewritingType];
-[TCTextCompositionAssistantWritingOptions setMaximumReflectionIterationCount:];
-[TCTextCompositionAssistantWritingOptions suppressValidation];
-[TCTextCompositionAssistantWritingOptions userPreferredLanguage];
-[TCTextCompositionAssistantWritingOptions userPreferredLanguages];
```
