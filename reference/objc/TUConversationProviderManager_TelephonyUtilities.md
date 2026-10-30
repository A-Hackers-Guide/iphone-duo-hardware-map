# `TUConversationProviderManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<TUConversationProviderManagerDataSource>" _dataSource;
```

## Properties

```
@property (T@"<TUConversationProviderManagerDataSource>",R,N,V_dataSource) dataSource;
```

## Instance methods

```
-[TUConversationProviderManager initWithDataSource:];
-[TUConversationProviderManager init];
-[TUConversationProviderManager dealloc];
-[TUConversationProviderManager dataSource];
-[TUConversationProviderManager registerConversationProviderForConfiguration:completionHandler:];
-[TUConversationProviderManager conversationProviderForIdentifier:completionHandler:];
-[TUConversationProviderManager doesHandle:correspondToConversationProvider:completionHandler:];
-[TUConversationProviderManager generatePseudonymHandleForConversationProvider:expiryDuration:URI:completionHandler:];
-[TUConversationProviderManager registerForCallbacksForProvider:completionHandler:];
-[TUConversationProviderManager renewPseudonymHandle:forConversationProvider:expirationDate:completionHandler:];
-[TUConversationProviderManager revokePseudonymHandle:forConversationProvider:completionHandler:];
```
