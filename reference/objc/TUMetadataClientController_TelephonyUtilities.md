# `TUMetadataClientController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"TUMetadataCache" _metadataCache;
```

## Properties

```
@property (T@"TUMetadataCache",&,N,V_metadataCache) metadataCache;
```

## Class methods

```
+[TUMetadataClientController sharedInstance];
```

## Instance methods

```
-[TUMetadataClientController init];
-[TUMetadataClientController metadataCache];
-[TUMetadataClientController setMetadataCache:];
-[TUMetadataClientController directoryLabelForDestinationID:];
-[TUMetadataClientController updateMetadataForDestinationID:];
-[TUMetadataClientController _metadataDestinationIdForSearchItem:];
-[TUMetadataClientController directoryLabelForSearchItem:];
-[TUMetadataClientController locationForDestinationID:];
-[TUMetadataClientController locationForSearchItem:];
-[TUMetadataClientController suggestionForDestinationID:];
-[TUMetadataClientController suggestionForSearchItem:];
-[TUMetadataClientController updateMetadataForCall:];
-[TUMetadataClientController updateMetadataForCall:completion:];
-[TUMetadataClientController updateMetadataForDestinationID:completion:];
-[TUMetadataClientController updateMetadataForRecentCalls:];
-[TUMetadataClientController updateMetadataForRecentCalls:completion:];
```
