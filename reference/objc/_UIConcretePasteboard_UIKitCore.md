# `_UIConcretePasteboard`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPasteboard`
- 3 instance variables, 3 properties, 84 instance methods, 19 class methods

## Instance variables

```
@"NSString" _name;
@"UISPasteSharingToken" _sharingToken;
@"NSObject<OS_dispatch_group>" _saveCompletionGroup;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"UISPasteSharingToken",C,V_sharingToken) sharingToken;
@property (T@"NSObject<OS_dispatch_group>",R,N,V_saveCompletionGroup) saveCompletionGroup;
```

## Class methods

```
+[_UIConcretePasteboard _detectPatternsForPatterns:atIndex:itemCollection:completionHandler:];
+[_UIConcretePasteboard _loadRequestContextForBlockingUIKitCall:];
+[_UIConcretePasteboard _pasteboardWithName:create:];
+[_UIConcretePasteboard pasteboardWithName:create:];
+[_UIConcretePasteboard _loadRequestContextForNonBlockingUIKitCall];
+[_UIConcretePasteboard pasteboardWithUniqueName];
+[_UIConcretePasteboard _pasteboardWithUniqueName];
+[_UIConcretePasteboard clientValueForValue:pattern:];
+[_UIConcretePasteboard _asynchronouslyEnumerateItemSet:itemsCompletionHandler:usingItemBlock:];
+[_UIConcretePasteboard _existingCachedPasteboardWithName:];
+[_UIConcretePasteboard _pinItemProviders:forPasteboardNamed:withExpirationDate:];
+[_UIConcretePasteboard _attemptAuthenticationWithMessage:];
+[_UIConcretePasteboard _pasteboardNamed:createIfNotFound:];
+[_UIConcretePasteboard _remoteContentForLayerContextWithId:slotStyle:pasteButtonTag:];
+[_UIConcretePasteboard _detectValuesForPatterns:atIndex:itemCollection:completionHandler:];
+[_UIConcretePasteboard _loadRequestContextForBlockingUIKitCall];
+[_UIConcretePasteboard removePasteboardWithName:];
+[_UIConcretePasteboard generalPasteboard];
+[_UIConcretePasteboard _clearPinnedItemProvidersForPasteboardNamed:];
```

## Instance methods

```
-[_UIConcretePasteboard setColors:];
-[_UIConcretePasteboard colors];
-[_UIConcretePasteboard numberOfItems];
-[_UIConcretePasteboard changeCount];
-[_UIConcretePasteboard detectPatternsForPatterns:completionHandler:];
-[_UIConcretePasteboard setColor:];
-[_UIConcretePasteboard itemProvidersForInstantiatingObjectsOfClass:];
-[_UIConcretePasteboard _clearItems];
-[_UIConcretePasteboard dataForPasteboardType:];
-[_UIConcretePasteboard containsPasteboardTypes:];
-[_UIConcretePasteboard pasteSharingToken];
-[_UIConcretePasteboard _saveTimestamp];
-[_UIConcretePasteboard setObjects:localOnly:expirationDate:];
-[_UIConcretePasteboard isPersistent];
-[_UIConcretePasteboard itemSetWithPasteboardTypes:];
-[_UIConcretePasteboard _changeCountIgnoringPinningActivity];
-[_UIConcretePasteboard valuesForPasteboardType:inItemSet:];
-[_UIConcretePasteboard pasteboardTypes];
-[_UIConcretePasteboard setItems:];
-[_UIConcretePasteboard sharingToken];
-[_UIConcretePasteboard _initWithName:];
-[_UIConcretePasteboard hasURLs];
-[_UIConcretePasteboard setItemProviders:options:];
-[_UIConcretePasteboard URLs];
-[_UIConcretePasteboard pasteboardTypesForItemSet:];
-[_UIConcretePasteboard hasStrings];
-[_UIConcretePasteboard itemProviders];
-[_UIConcretePasteboard detectValuesForPatterns:inItemSet:completionHandler:];
-[_UIConcretePasteboard string];
-[_UIConcretePasteboard valueForPasteboardType:];
-[_UIConcretePasteboard images];
-[_UIConcretePasteboard _setItemsAndSaveFromObjects:ofClass:];
-[_UIConcretePasteboard setString:];
-[_UIConcretePasteboard items];
-[_UIConcretePasteboard _pinItemCollection:];
-[_UIConcretePasteboard _pasteboardCacheQueue_setPersistent:currentNotificationState:outNewNotificationState:];
-[_UIConcretePasteboard setData:forPasteboardType:];
-[_UIConcretePasteboard canInstantiateObjectsOfClass:];
-[_UIConcretePasteboard _pasteboardCacheQueue_isPersistent];
-[_UIConcretePasteboard _saveItemCollection:];
-[_UIConcretePasteboard setValue:forPasteboardType:];
-[_UIConcretePasteboard color];
-[_UIConcretePasteboard detectPatternsForPatterns:inItemSet:completionHandler:];
-[_UIConcretePasteboard _setItemsAndSave:options:];
-[_UIConcretePasteboard _detectedPasteboardTypeStringsForTypes:];
-[_UIConcretePasteboard _requestSecurePasteAuthenticationMessageWithContext:forClientVersionedPID:completionBlock:];
-[_UIConcretePasteboard _pinItemProviders:expirationDate:];
-[_UIConcretePasteboard setURL:];
-[_UIConcretePasteboard _setPersistent:];
-[_UIConcretePasteboard setPersistent:];
-[_UIConcretePasteboard _originatorLocalizedName];
-[_UIConcretePasteboard setObjects:options:];
-[_UIConcretePasteboard detectValuesForPatterns:completionHandler:];
-[_UIConcretePasteboard _sendPasteboardTypesChangedNotificationOldTypes:newTypes:];
-[_UIConcretePasteboard _itemsCoercibleToClass:];
-[_UIConcretePasteboard setItemProviders:localOnly:expirationDate:];
-[_UIConcretePasteboard setObjects:];
-[_UIConcretePasteboard setImages:];
-[_UIConcretePasteboard setURLs:];
-[_UIConcretePasteboard setItemProviders:];
-[_UIConcretePasteboard itemProvidersWithRetryBehavior:];
-[_UIConcretePasteboard strings];
-[_UIConcretePasteboard setName:];
-[_UIConcretePasteboard hasColors];
-[_UIConcretePasteboard saveCompletionGroup];
-[_UIConcretePasteboard hasImages];
-[_UIConcretePasteboard setSharingToken:];
-[_UIConcretePasteboard image];
-[_UIConcretePasteboard _pasteboardCacheQueue_saveItemCollection:currentNotificationState:outNewNotificationState:];
-[_UIConcretePasteboard _clearPinnedItemProviders];
-[_UIConcretePasteboard _preauthorizePasteForAuditToken:pasteboardName:changeCount:completionBlock:];
-[_UIConcretePasteboard _setItemsAndSave:options:coerceStringsToURLs:dataOwner:];
-[_UIConcretePasteboard setItems:options:];
-[_UIConcretePasteboard containsPasteboardTypes:inItemSet:];
-[_UIConcretePasteboard name];
-[_UIConcretePasteboard addItems:];
-[_UIConcretePasteboard _setItemsAndSave:options:coerceStringsToURLs:];
-[_UIConcretePasteboard setStrings:];
-[_UIConcretePasteboard URL];
-[_UIConcretePasteboard _detectedPasteboardTypesForTypes:];
-[_UIConcretePasteboard _originatorBundleID];
-[_UIConcretePasteboard availableTypes];
-[_UIConcretePasteboard dataForPasteboardType:inItemSet:];
-[_UIConcretePasteboard setImage:];
```
