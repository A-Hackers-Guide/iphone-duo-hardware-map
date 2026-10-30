# `CUINamedLookup`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSLocking`
- 7 instance variables, 22 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"CUIRenditionKey" _key;
@"NSString" _signature;
Q _storageRef;
I _distilledInVersion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
b1 _odContent;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"CUIRenditionKey",C,N,V_key) key;
@property (TQ,N,V_storageRef) storageRef;
@property (T@"CUIThemeRendition",R,N) _rendition;
@property (T@"CUIRenditionKey",R,N) renditionKey;
@property (T@"NSString",R,N) keySignature;
@property (TB,R,N) _cacheRenditionProperties;
@property (TI,N,S_setDistilledInVersion:,V_distilledInVersion) _distilledInVersion;
@property (TQ,R,N) subtype;
@property (Tq,R,N) sizeClassHorizontal;
@property (Tq,R,N) sizeClassVertical;
@property (Tq,R,N) memoryClass;
@property (Tq,R,N) graphicsClass;
@property (Tq,R,N) appearanceIdentifier;
@property (T@"NSString",R,N) renditionName;
@property (TB,R,N) representsOnDemandContent;
@property (Tq,R,N) idiom;
@property (Tq,R,N) displayGamut;
@property (Tq,R,N) layoutDirection;
@property (Tq,R,N) localization;
@property (T@"NSString",R,N) appearance;
@property (Td,R,N) scale;
```

## Instance methods

```
-[CUINamedLookup subtype];
-[CUINamedLookup displayGamut];
-[CUINamedLookup appearanceIdentifier];
-[CUINamedLookup dealloc];
-[CUINamedLookup layoutDirection];
-[CUINamedLookup sizeClassHorizontal];
-[CUINamedLookup setKey:];
-[CUINamedLookup initWithName:usingRenditionKey:fromTheme:];
-[CUINamedLookup localization];
-[CUINamedLookup scale];
-[CUINamedLookup sizeClassVertical];
-[CUINamedLookup hash];
-[CUINamedLookup setName:];
-[CUINamedLookup appearance];
-[CUINamedLookup lock];
-[CUINamedLookup renditionKey];
-[CUINamedLookup isEqual:];
-[CUINamedLookup unlock];
-[CUINamedLookup name];
-[CUINamedLookup _updateFromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedLookup key];
-[CUINamedLookup idiom];
-[CUINamedLookup representsOnDemandContent];
-[CUINamedLookup keySignature];
-[CUINamedLookup _cacheRenditionProperties];
-[CUINamedLookup _distilledInVersion];
-[CUINamedLookup _rendition];
-[CUINamedLookup _renditionForSpecificKey:];
-[CUINamedLookup _setDistilledInVersion:];
-[CUINamedLookup graphicsClass];
-[CUINamedLookup isTintable];
-[CUINamedLookup memoryClass];
-[CUINamedLookup renditionName];
-[CUINamedLookup setRepresentsOnDemandContent:];
-[CUINamedLookup setStorageRef:];
-[CUINamedLookup storageRef];
```
