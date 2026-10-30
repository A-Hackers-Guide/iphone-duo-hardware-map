# `SBLeafIconDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 41 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) uniqueIdentifier;
@property (T@"NSString",?,R,C,N) configurationStorageIdentifier;
```

## Instance methods

```
-[SBLeafIconDataSource uniqueIdentifier];
-[SBLeafIconDataSource icon:displayNameForLocation:];
-[SBLeafIconDataSource labelAccessoryTypeForIcon:];
-[SBLeafIconDataSource icon:displayNameForObscuredDisabledLaunchForLocation:];
-[SBLeafIconDataSource iconShouldBeDimmed:];
-[SBLeafIconDataSource supportedGridSizeClassesForIcon:];
-[SBLeafIconDataSource iconCanTightenLabel:];
-[SBLeafIconDataSource iconSupportsUninstall:];
-[SBLeafIconDataSource icon:launchFromLocation:context:];
-[SBLeafIconDataSource iconCompleteUninstall:];
-[SBLeafIconDataSource iconSupportsConfiguration:];
-[SBLeafIconDataSource iconCanTruncateLabel:];
-[SBLeafIconDataSource applicationBundleIdentifierForImageForIcon:];
-[SBLeafIconDataSource iconAllowsLaunch:];
-[SBLeafIconDataSource folderTitleOptionsForIcon:];
-[SBLeafIconDataSource icon:imageWithInfo:];
-[SBLeafIconDataSource priorityForIcon:];
-[SBLeafIconDataSource isTimedOutForIcon:];
-[SBLeafIconDataSource iconDisallowsLaunchForObscuredReason:];
-[SBLeafIconDataSource iTunesCategoriesOrderedByRelevancyForIcon:];
-[SBLeafIconDataSource folderFallbackTitleForIcon:];
-[SBLeafIconDataSource configurationStorageIdentifier];
-[SBLeafIconDataSource badgeNumberOrStringForIcon:];
-[SBLeafIconDataSource dataOwnershipRoleAsDragDropTargetForIcon:];
-[SBLeafIconDataSource tagsForIcon:];
-[SBLeafIconDataSource icon:statusDescriptionForLocation:];
-[SBLeafIconDataSource accessoryTypeForIcon:];
-[SBLeafIconDataSource canGenerateIconsInBackgroundForIcon:];
-[SBLeafIconDataSource formattedAccessoryStringForIcon:];
-[SBLeafIconDataSource icon:defaultImageWithInfo:];
-[SBLeafIconDataSource icon:imageWithInfo:traitCollection:options:];
-[SBLeafIconDataSource icon:layerWithInfo:traitCollection:options:];
-[SBLeafIconDataSource icon:unmaskedImageWithInfo:];
-[SBLeafIconDataSource iconRepresentsExternalContent:];
-[SBLeafIconDataSource iconServicesIconForImageForIcon:];
-[SBLeafIconDataSource iconShouldIgnoreOtherDataSources:];
-[SBLeafIconDataSource iconSupportsRasterization:];
-[SBLeafIconDataSource iconTypeIdentifierForImageForIcon:];
-[SBLeafIconDataSource isProgressPausedForIcon:];
-[SBLeafIconDataSource progressPercentForIcon:];
-[SBLeafIconDataSource progressStateForIcon:];
```
