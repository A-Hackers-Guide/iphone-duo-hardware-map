# `TUCallDirectoryMetadataCacheDataProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUMetadataCacheDataProvider`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _cacheOnly;
i _identificationEntriesChangedNotifyToken;
@"CXCallDirectoryManager" _callDirectoryManager;
@? _countryDialingCode;
@? _firstIdentificationEntriesForEnabledExtensions;
```

## Properties

```
@property (T@"CXCallDirectoryManager",R,N,V_callDirectoryManager) callDirectoryManager;
@property (Ti,R,N,V_identificationEntriesChangedNotifyToken) identificationEntriesChangedNotifyToken;
@property (T@?,C,N,V_countryDialingCode) countryDialingCode;
@property (T@?,C,N,V_firstIdentificationEntriesForEnabledExtensions) firstIdentificationEntriesForEnabledExtensions;
@property (TB,R,N,V_cacheOnly) cacheOnly;
```

## Instance methods

```
-[TUCallDirectoryMetadataCacheDataProvider cacheOnly];
-[TUCallDirectoryMetadataCacheDataProvider init];
-[TUCallDirectoryMetadataCacheDataProvider dealloc];
-[TUCallDirectoryMetadataCacheDataProvider callDirectoryManager];
-[TUCallDirectoryMetadataCacheDataProvider countryDialingCode];
-[TUCallDirectoryMetadataCacheDataProvider firstIdentificationEntriesForEnabledExtensions];
-[TUCallDirectoryMetadataCacheDataProvider identificationEntriesChangedNotifyToken];
-[TUCallDirectoryMetadataCacheDataProvider initWithCacheOnly:];
-[TUCallDirectoryMetadataCacheDataProvider setCountryDialingCode:];
-[TUCallDirectoryMetadataCacheDataProvider setFirstIdentificationEntriesForEnabledExtensions:];
-[TUCallDirectoryMetadataCacheDataProvider updateCacheWithDestinationIDs:withGroup:];
```
