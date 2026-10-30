# `SBDisplayItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 7 instance variables, 8 properties, 30 instance methods, 10 class methods

## Instance variables

```
@"NSString" _uniqueStringRepresentation;
Q _uniqueStringRepresentationHash;
@? _sceneIdentifierFromBundleIdentifierGenerator;
Q _hash;
q _type;
@"NSString" _bundleIdentifier;
@"NSString" _uniqueIdentifier;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,C,N) webClipIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDisplayItem appLibraryDisplayItem];
+[SBDisplayItem applicationDisplayItemWithBundleIdentifier:sceneIdentifier:];
+[SBDisplayItem displayItemForLayoutElement:];
+[SBDisplayItem displayItemForWorkspaceEntity:];
+[SBDisplayItem displayItemWithProtobufRepresentation:];
+[SBDisplayItem displayItemWithType:bundleIdentifier:uniqueIdentifier:];
+[SBDisplayItem homeScreenDisplayItem];
+[SBDisplayItem remoteAlertDisplayItemWithServiceBundleIdentifier:];
+[SBDisplayItem switcherServiceDisplayItemWithServiceIdentifier:];
+[SBDisplayItem webAppDisplayItemWithWebAppIdentifier:];
```

## Instance methods

```
-[SBDisplayItem isAppLibraryDisplayItem];
-[SBDisplayItem isEqualToDisplayItemForFloatingDockSuggestions:];
-[SBDisplayItem isHomeScreenDisplayItem];
-[SBDisplayItem succinctDescriptionBuilder];
-[SBDisplayItem compare:];
-[SBDisplayItem init];
-[SBDisplayItem bundleIdentifier];
-[SBDisplayItem _newSceneIdentifierForBundleIdentifier:];
-[SBDisplayItem descriptionWithMultilinePrefix:];
-[SBDisplayItem _initWithDictionaryPlistRepresentation:];
-[SBDisplayItem uniqueIdentifier];
-[SBDisplayItem webClipIdentifier];
-[SBDisplayItem protobufRepresentation];
-[SBDisplayItem _initWithLegacyPlistRepresentation:sceneIdentifierFromBundleIdentifierGenerator:];
-[SBDisplayItem succinctDescription];
-[SBDisplayItem _calculateUniqueStringRepresentation];
-[SBDisplayItem _initWithArrayPlistRepresentation:];
-[SBDisplayItem type];
-[SBDisplayItem uniqueStringRepresentation];
-[SBDisplayItem plistRepresentation];
-[SBDisplayItem hash];
-[SBDisplayItem description];
-[SBDisplayItem initWithPlistRepresentation:];
-[SBDisplayItem initWithType:bundleIdentifier:uniqueIdentifier:];
-[SBDisplayItem copyWithZone:];
-[SBDisplayItem isEqual:];
-[SBDisplayItem displayItemForFloatingDockSuggestionsComparison];
-[SBDisplayItem initWithLegacyPlistRepresentation:];
-[SBDisplayItem _initWithPlistRepresentation:sceneIdentifierFromBundleIdentifierGenerator:];
-[SBDisplayItem descriptionBuilderWithMultilinePrefix:];
```
