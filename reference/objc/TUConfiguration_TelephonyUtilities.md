# `TUConfiguration`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConfiguration`
- 2 instance variables, 11 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<TUKeyValueDataSource><TUMutableKeyValueDataSource>" _dataSource;
@"TUDelegateController" _delegateController;
```

## Properties

```
@property (T@"TUDelegateController",R,N,V_delegateController) delegateController;
@property (TQ,N) announceCalls;
@property (T@"NSString",&,N) conversationLinkBaseURLString;
@property (T@"NSURL",&,N) conversationLinkBaseURL;
@property (TB,N) simulateFatalPersistentStoreError;
@property (TB,N) simulateInternationalCall;
@property (T@"<TUKeyValueDataSource><TUMutableKeyValueDataSource>",R,N,V_dataSource) dataSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUConfiguration initWithDataSource:];
-[TUConfiguration removeDelegate:];
-[TUConfiguration addDelegate:queue:];
-[TUConfiguration dataSource];
-[TUConfiguration numberForKey:];
-[TUConfiguration announceCalls];
-[TUConfiguration delegateController];
-[TUConfiguration conversationLinkBaseURL];
-[TUConfiguration conversationLinkBaseURLString];
-[TUConfiguration setAnnounceCalls:];
-[TUConfiguration setConversationLinkBaseURL:];
-[TUConfiguration setConversationLinkBaseURLString:];
-[TUConfiguration setSimulateFatalPersistentStoreError:];
-[TUConfiguration setSimulateInternationalCall:];
-[TUConfiguration simulateFatalPersistentStoreError];
-[TUConfiguration simulateInternationalCall];
```
