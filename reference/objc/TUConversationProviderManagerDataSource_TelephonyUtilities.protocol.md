# `TUConversationProviderManagerDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance methods

```
-[TUConversationProviderManagerDataSource invalidate];
-[TUConversationProviderManagerDataSource conversationProviderForIdentifier:];
-[TUConversationProviderManagerDataSource conversationProviderForIdentifier:completionHandler:];
-[TUConversationProviderManagerDataSource doesHandle:correspondToConversationProvider:completionHandler:];
-[TUConversationProviderManagerDataSource generatePseudonymHandleForConversationProvider:expiryDuration:URI:completionHandler:];
-[TUConversationProviderManagerDataSource registerConversationProvider:completionHandler:];
-[TUConversationProviderManagerDataSource registerForCallbacksForProvider:completionHandler:];
-[TUConversationProviderManagerDataSource renewPseudonymHandle:forConversationProvider:expirationDate:completionHandler:];
-[TUConversationProviderManagerDataSource revokePseudonymHandle:forConversationProvider:completionHandler:];
```
