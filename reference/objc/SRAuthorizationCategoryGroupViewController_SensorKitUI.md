# `SRAuthorizationCategoryGroupViewController`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- Protocols: `SRAuthorizationCellDelegate`, `UITableViewDelegatePrivate`
- 6 instance variables, 10 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSBundle" _appBundle;
@"NSMutableDictionary" _readerAuthState;
@"NSMutableDictionary" _writerAuthState;
@"SRAuthorizationStore" _authStore;
@"NSArray" _sortedReaderAuthorizationServices;
@"NSArray" _sortedWriterAuthorizationServices;
```

## Properties

```
@property (T@"NSArray",&,N,V_sortedReaderAuthorizationServices) sortedReaderAuthorizationServices;
@property (T@"NSArray",&,N,V_sortedWriterAuthorizationServices) sortedWriterAuthorizationServices;
@property (T@"NSBundle",&,N,V_appBundle) appBundle;
@property (T@"NSMutableDictionary",&,N,V_readerAuthState) readerAuthState;
@property (T@"NSMutableDictionary",&,N,V_writerAuthState) writerAuthState;
@property (T@"SRAuthorizationStore",&,V_authStore) authStore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SRAuthorizationCategoryGroupViewController tableView:numberOfRowsInSection:];
-[SRAuthorizationCategoryGroupViewController numberOfSectionsInTableView:];
-[SRAuthorizationCategoryGroupViewController tableView:cellForRowAtIndexPath:];
-[SRAuthorizationCategoryGroupViewController init];
-[SRAuthorizationCategoryGroupViewController dealloc];
-[SRAuthorizationCategoryGroupViewController tableView:titleForHeaderInSection:];
-[SRAuthorizationCategoryGroupViewController viewDidLoad];
-[SRAuthorizationCategoryGroupViewController tableView:didSelectRowAtIndexPath:];
-[SRAuthorizationCategoryGroupViewController appBundle];
-[SRAuthorizationCategoryGroupViewController setAppBundle:];
-[SRAuthorizationCategoryGroupViewController authStore];
-[SRAuthorizationCategoryGroupViewController setAuthStore:];
-[SRAuthorizationCategoryGroupViewController readerAuthState];
-[SRAuthorizationCategoryGroupViewController writerAuthState];
-[SRAuthorizationCategoryGroupViewController authorizationSwitchToggledWithValue:indexPath:];
-[SRAuthorizationCategoryGroupViewController confirmAuthChangeForService:value:indexPath:setOverride:];
-[SRAuthorizationCategoryGroupViewController indexPathIsInWriterSection:];
-[SRAuthorizationCategoryGroupViewController openPrivacy];
-[SRAuthorizationCategoryGroupViewController readerAuthSectionStart];
-[SRAuthorizationCategoryGroupViewController serviceFromIndexPath:];
-[SRAuthorizationCategoryGroupViewController setReaderAuthState:];
-[SRAuthorizationCategoryGroupViewController setSortedReaderAuthorizationServices:];
-[SRAuthorizationCategoryGroupViewController setSortedWriterAuthorizationServices:];
-[SRAuthorizationCategoryGroupViewController setWriterAuthState:];
-[SRAuthorizationCategoryGroupViewController sortedReaderAuthorizationServices];
-[SRAuthorizationCategoryGroupViewController sortedWriterAuthorizationServices];
-[SRAuthorizationCategoryGroupViewController usageSectionStart];
-[SRAuthorizationCategoryGroupViewController writerAuthSectionStart];
```
