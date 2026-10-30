# `TUSuggestionsMetadataCacheDataProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUMetadataCacheDataProvider`
- 2 instance variables, 2 properties, 5 instance methods, 8 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" _suggestionsServiceThrottleSemaphore;
@ _suggestionsContactsObserver;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_suggestionsServiceThrottleSemaphore) suggestionsServiceThrottleSemaphore;
@property (T@,R,N,V_suggestionsContactsObserver) suggestionsContactsObserver;
```

## Class methods

```
+[TUSuggestionsMetadataCacheDataProvider sharedService];
+[TUSuggestionsMetadataCacheDataProvider canUseSiriSuggestions];
+[TUSuggestionsMetadataCacheDataProvider newestSuggestedContactForDestinationID:];
+[TUSuggestionsMetadataCacheDataProvider shouldQuerySupportsInfo];
+[TUSuggestionsMetadataCacheDataProvider suggestedNameForDestinationID:onlySignificant:error:];
+[TUSuggestionsMetadataCacheDataProvider suggestedNamesForDestinationID:onlySignificant:error:];
+[TUSuggestionsMetadataCacheDataProvider suggestedNamesForDestinationID:onlySignificant:supportsInfoLookup:error:];
+[TUSuggestionsMetadataCacheDataProvider suggestedNamesForDestinationID:onlySignificant:withCompletion:];
```

## Instance methods

```
-[TUSuggestionsMetadataCacheDataProvider init];
-[TUSuggestionsMetadataCacheDataProvider setSuggestionsServiceThrottleSemaphore:];
-[TUSuggestionsMetadataCacheDataProvider suggestionsContactsObserver];
-[TUSuggestionsMetadataCacheDataProvider suggestionsServiceThrottleSemaphore];
-[TUSuggestionsMetadataCacheDataProvider updateCacheWithDestinationIDs:withGroup:];
```
