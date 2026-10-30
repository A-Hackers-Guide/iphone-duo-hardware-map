# `TUConversationMediaController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationMediaControllerDataSourceDelegate`
- 2 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<TUConversationManagerDataSource>" _dataSource;
@"NSHashTable" _delegates;
```

## Properties

```
@property (T@"<TUConversationManagerDataSource>",R,N,V_dataSource) dataSource;
@property (T@"NSHashTable",&,N,V_delegates) delegates;
@property (T@"<TUConversationMediaControllerDelegate>",W,N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUConversationMediaController removeDelegate:];
-[TUConversationMediaController setDelegates:];
-[TUConversationMediaController delegates];
-[TUConversationMediaController addDelegate:];
-[TUConversationMediaController setDelegate:];
-[TUConversationMediaController dataSource];
-[TUConversationMediaController delegate];
-[TUConversationMediaController updateConversationWithUUID:participantPresentationContexts:];
-[TUConversationMediaController initWithConversationDataSource:];
-[TUConversationMediaController mediaPrioritiesChangeForConversation:];
```
