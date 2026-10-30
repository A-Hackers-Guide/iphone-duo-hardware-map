# `TCTextCompositionAssistantSmartResponseOptions`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 15 instance variables, 15 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isPrecomputationRequest;
B _respondOnlyIfCached;
B _smartQuotesEnabled;
B _smartDashesEnabled;
B _isExternalAPICall;
Q _token;
Q _maximumReplyCount;
Q _pid;
@"NSString" _bundleId;
@"NSString" _requestIdentifier;
Q _textAutocapitalizationOn;
@"NSArray" _userQuotesArray;
@"NSString" _userPreferredLanguage;
Q _regionPolicy;
@"NSString" _customArchetypeProfilesJSON;
```

## Properties

```
@property (TQ,R,N,V_token) token;
@property (TQ,R,N,V_maximumReplyCount) maximumReplyCount;
@property (TQ,R,N,V_pid) pid;
@property (T@"NSString",R,C,N,V_bundleId) bundleId;
@property (T@"NSString",R,C,N,V_requestIdentifier) requestIdentifier;
@property (TB,R,N,V_isPrecomputationRequest) isPrecomputationRequest;
@property (TB,R,N,V_respondOnlyIfCached) respondOnlyIfCached;
@property (TQ,R,N,V_textAutocapitalizationOn) textAutocapitalizationOn;
@property (TB,R,V_smartQuotesEnabled) smartQuotesEnabled;
@property (TB,R,V_smartDashesEnabled) smartDashesEnabled;
@property (T@"NSArray",R,C,V_userQuotesArray) userQuotesArray;
@property (T@"NSString",R,C,V_userPreferredLanguage) userPreferredLanguage;
@property (TQ,R,N,V_regionPolicy) regionPolicy;
@property (TB,R,N,V_isExternalAPICall) isExternalAPICall;
@property (T@"NSString",R,N,V_customArchetypeProfilesJSON) customArchetypeProfilesJSON;
```

## Instance methods

```
-[TCTextCompositionAssistantSmartResponseOptions smartQuotesEnabled];
-[TCTextCompositionAssistantSmartResponseOptions requestIdentifier];
-[TCTextCompositionAssistantSmartResponseOptions initWithOptions:];
-[TCTextCompositionAssistantSmartResponseOptions pid];
-[TCTextCompositionAssistantSmartResponseOptions smartDashesEnabled];
-[TCTextCompositionAssistantSmartResponseOptions bundleId];
-[TCTextCompositionAssistantSmartResponseOptions token];
-[TCTextCompositionAssistantSmartResponseOptions copyWithZone:];
-[TCTextCompositionAssistantSmartResponseOptions regionPolicy];
-[TCTextCompositionAssistantSmartResponseOptions userQuotesArray];
-[TCTextCompositionAssistantSmartResponseOptions customArchetypeProfilesJSON];
-[TCTextCompositionAssistantSmartResponseOptions isExternalAPICall];
-[TCTextCompositionAssistantSmartResponseOptions isPrecomputationRequest];
-[TCTextCompositionAssistantSmartResponseOptions maximumReplyCount];
-[TCTextCompositionAssistantSmartResponseOptions respondOnlyIfCached];
-[TCTextCompositionAssistantSmartResponseOptions textAutocapitalizationOn];
-[TCTextCompositionAssistantSmartResponseOptions userPreferredLanguage];
```
