# `UIActivityItemsConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIActivityItemsConfigurationReading`
- 11 instance variables, 16 properties, 30 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _itemProviders;
@"NSArray" _activityItems;
@"UIActivityViewController" _vc;
@"NSArray" _excludedActivityTypes;
@ _localObject;
@"NSArray" _supportedInteractions;
@? _metadataProvider;
@? _perItemMetadataProvider;
@? _previewProvider;
@? _applicationActivitiesProvider;
@"NSArray" __excludedInteractions;
```

## Properties

```
@property (TB,R,N) _hasItemsForActivityItemsConfiguration;
@property (T@"NSArray",R,C,N) _activityItems;
@property (T@"NSArray",C,N,S_setExcludedActivityTypes:) _excludedActivityTypes;
@property (T@"NSArray",C,N,S_setExcludedInteractions:,V__excludedInteractions) _excludedInteractions;
@property (T@,&,N,V_localObject) localObject;
@property (T@"NSArray",C,N,V_supportedInteractions) supportedInteractions;
@property (T@?,C,N,V_metadataProvider) metadataProvider;
@property (T@?,C,N,V_perItemMetadataProvider) perItemMetadataProvider;
@property (T@?,C,N,V_previewProvider) previewProvider;
@property (T@?,C,N,V_applicationActivitiesProvider) applicationActivitiesProvider;
@property (T@"NSArray",R,C,N) itemProvidersForActivityItemsConfiguration;
@property (T@"NSArray",?,R,C,N) applicationActivitiesForActivityItemsConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIActivityItemsConfiguration _itemsForSystemSharingFromActivityItemsConfiguration:wrapperBlock:];
+[UIActivityItemsConfiguration activityItemsConfigurationWithItemProviders:];
+[UIActivityItemsConfiguration activityItemsConfigurationWithObjects:];
```

## Instance methods

```
-[UIActivityItemsConfiguration _commonInit];
-[UIActivityItemsConfiguration setLocalObject:];
-[UIActivityItemsConfiguration localObject];
-[UIActivityItemsConfiguration initWithObjects:];
-[UIActivityItemsConfiguration setPreviewProvider:];
-[UIActivityItemsConfiguration itemProviders];
-[UIActivityItemsConfiguration metadataProvider];
-[UIActivityItemsConfiguration previewProvider];
-[UIActivityItemsConfiguration _activityItems];
-[UIActivityItemsConfiguration _excludedActivityTypes];
-[UIActivityItemsConfiguration _excludedInteractions];
-[UIActivityItemsConfiguration _hasItemsForActivityItemsConfiguration];
-[UIActivityItemsConfiguration _initWithActivityItemSources:];
-[UIActivityItemsConfiguration _initWithActivityItems:applicationActivities:];
-[UIActivityItemsConfiguration _setExcludedActivityTypes:];
-[UIActivityItemsConfiguration _setExcludedInteractions:];
-[UIActivityItemsConfiguration activityItemsConfigurationMetadataForItemAtIndex:key:];
-[UIActivityItemsConfiguration activityItemsConfigurationMetadataForKey:];
-[UIActivityItemsConfiguration activityItemsConfigurationPreviewForItemAtIndex:intent:suggestedSize:];
-[UIActivityItemsConfiguration activityItemsConfigurationSupportsInteraction:];
-[UIActivityItemsConfiguration applicationActivitiesForActivityItemsConfiguration];
-[UIActivityItemsConfiguration applicationActivitiesProvider];
-[UIActivityItemsConfiguration initWithItemProviders:];
-[UIActivityItemsConfiguration itemProvidersForActivityItemsConfiguration];
-[UIActivityItemsConfiguration perItemMetadataProvider];
-[UIActivityItemsConfiguration setApplicationActivitiesProvider:];
-[UIActivityItemsConfiguration setMetadataProvider:];
-[UIActivityItemsConfiguration setPerItemMetadataProvider:];
-[UIActivityItemsConfiguration setSupportedInteractions:];
-[UIActivityItemsConfiguration supportedInteractions];
```
