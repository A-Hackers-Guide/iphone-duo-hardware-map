# `UIPasteboard`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 24 properties, 67 instance methods, 14 class methods

## Instance variables

```
Q __saveTimestamp;
@"NSString" __originatorLocalizedName;
@"NSString" __originatorBundleID;
```

## Properties

```
@property (T@"NSArray",R,C,N) availableTypes;
@property (Tq,R,N) _changeCountIgnoringPinningActivity;
@property (TQ,R,N,V__saveTimestamp) _saveTimestamp;
@property (T@"NSString",R,C,N,V__originatorLocalizedName) _originatorLocalizedName;
@property (T@"NSString",R,C,N,V__originatorBundleID) _originatorBundleID;
@property (T@"NSString",R,N) name;
@property (TB,R,N,GisPersistent) persistent;
@property (Tq,R,N) changeCount;
@property (T@"NSArray",C,N) itemProviders;
@property (T@"NSArray",R,N) pasteboardTypes;
@property (Tq,R,N) numberOfItems;
@property (T@"NSArray",C,N) items;
@property (T@"NSString",C,N) string;
@property (T@"NSArray",C,N) strings;
@property (T@"NSURL",C,N) URL;
@property (T@"NSArray",C,N) URLs;
@property (T@"UIImage",C,N) image;
@property (T@"NSArray",C,N) images;
@property (T@"UIColor",C,N) color;
@property (T@"NSArray",C,N) colors;
@property (TB,R,N) hasStrings;
@property (TB,R,N) hasURLs;
@property (TB,R,N) hasImages;
@property (TB,R,N) hasColors;
```

## Class methods

```
+[UIPasteboard _pasteboardWithName:create:];
+[UIPasteboard pasteboardWithName:create:];
+[UIPasteboard pasteboardWithUniqueName];
+[UIPasteboard _pasteboardWithUniqueName];
+[UIPasteboard _existingCachedPasteboardWithName:];
+[UIPasteboard _pinItemProviders:forPasteboardNamed:withExpirationDate:];
+[UIPasteboard _attemptAuthenticationWithMessage:];
+[UIPasteboard removePasteboardWithName:];
+[UIPasteboard generalPasteboard];
+[UIPasteboard _clearPinnedItemProvidersForPasteboardNamed:];
+[UIPasteboard _getDataOwner:forAction:responder:];
+[UIPasteboard _performAsDataOwner:block:];
+[UIPasteboard pasteSharingTokenFromOpenURL];
+[UIPasteboard setPasteSharingTokenFromOpenURL:];
```

## Instance methods

```
-[UIPasteboard setColors:];
-[UIPasteboard colors];
-[UIPasteboard numberOfItems];
-[UIPasteboard changeCount];
-[UIPasteboard detectPatternsForPatterns:completionHandler:];
-[UIPasteboard setColor:];
-[UIPasteboard itemProvidersForInstantiatingObjectsOfClass:];
-[UIPasteboard dataForPasteboardType:];
-[UIPasteboard containsPasteboardTypes:];
-[UIPasteboard pasteSharingToken];
-[UIPasteboard _saveTimestamp];
-[UIPasteboard setObjects:localOnly:expirationDate:];
-[UIPasteboard isPersistent];
-[UIPasteboard itemSetWithPasteboardTypes:];
-[UIPasteboard _changeCountIgnoringPinningActivity];
-[UIPasteboard valuesForPasteboardType:inItemSet:];
-[UIPasteboard pasteboardTypes];
-[UIPasteboard setItems:];
-[UIPasteboard hasURLs];
-[UIPasteboard setItemProviders:options:];
-[UIPasteboard URLs];
-[UIPasteboard pasteboardTypesForItemSet:];
-[UIPasteboard hasStrings];
-[UIPasteboard itemProviders];
-[UIPasteboard detectValuesForPatterns:inItemSet:completionHandler:];
-[UIPasteboard string];
-[UIPasteboard valueForPasteboardType:];
-[UIPasteboard images];
-[UIPasteboard setString:];
-[UIPasteboard items];
-[UIPasteboard setData:forPasteboardType:];
-[UIPasteboard canInstantiateObjectsOfClass:];
-[UIPasteboard setValue:forPasteboardType:];
-[UIPasteboard color];
-[UIPasteboard detectPatternsForPatterns:inItemSet:completionHandler:];
-[UIPasteboard _detectedPasteboardTypeStringsForTypes:];
-[UIPasteboard _requestSecurePasteAuthenticationMessageWithContext:forClientVersionedPID:completionBlock:];
-[UIPasteboard _pinItemProviders:expirationDate:];
-[UIPasteboard setURL:];
-[UIPasteboard setPersistent:];
-[UIPasteboard _originatorLocalizedName];
-[UIPasteboard setObjects:options:];
-[UIPasteboard detectValuesForPatterns:completionHandler:];
-[UIPasteboard setItemProviders:localOnly:expirationDate:];
-[UIPasteboard setObjects:];
-[UIPasteboard setImages:];
-[UIPasteboard setURLs:];
-[UIPasteboard setItemProviders:];
-[UIPasteboard strings];
-[UIPasteboard setName:];
-[UIPasteboard hasColors];
-[UIPasteboard hasImages];
-[UIPasteboard image];
-[UIPasteboard _clearPinnedItemProviders];
-[UIPasteboard _preauthorizePasteForAuditToken:pasteboardName:changeCount:completionBlock:];
-[UIPasteboard setItems:options:];
-[UIPasteboard containsPasteboardTypes:inItemSet:];
-[UIPasteboard name];
-[UIPasteboard addItems:];
-[UIPasteboard setStrings:];
-[UIPasteboard URL];
-[UIPasteboard _detectedPasteboardTypesForTypes:];
-[UIPasteboard _originatorBundleID];
-[UIPasteboard availableTypes];
-[UIPasteboard dataForPasteboardType:inItemSet:];
-[UIPasteboard setImage:];
-[UIPasteboard _hasStrings];
```
