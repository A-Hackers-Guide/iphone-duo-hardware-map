# `TUConversationReactionsController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationReactionsControllerDataSourceDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<TUConversationManagerDataSource>" _dataSource;
@"NSHashTable" _delegates;
```

## Properties

```
@property (T@"<TUConversationManagerDataSource>",R,N,V_dataSource) dataSource;
@property (T@"NSHashTable",&,N,V_delegates) delegates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUConversationReactionsController removeDelegate:];
-[TUConversationReactionsController setDelegates:];
-[TUConversationReactionsController delegates];
-[TUConversationReactionsController addDelegate:];
-[TUConversationReactionsController conversation:participantDidStopReacting:];
-[TUConversationReactionsController dataSource];
-[TUConversationReactionsController conversation:participant:didReact:];
-[TUConversationReactionsController initWithConversationDataSource:];
```
