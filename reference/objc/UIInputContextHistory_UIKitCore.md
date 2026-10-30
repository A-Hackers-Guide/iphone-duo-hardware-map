# `UIInputContextHistory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"TIInputContextHistory" _tiInputContextHistory;
```

## Properties

```
@property (T@"NSSet",R,N) senderIdentifiers;
@property (T@"NSSet",R,N) recipientIdentifiers;
@property (T@"TIInputContextHistory",R,N,V_tiInputContextHistory) tiInputContextHistory;
@property (T@"NSSet",R,N) recipientNames;
@property (T@"NSString",R,N) senderIdentifier;
```

## Instance methods

```
-[UIInputContextHistory senderIdentifiers];
-[UIInputContextHistory addEntry:];
-[UIInputContextHistory updateRecipientNames:];
-[UIInputContextHistory recipientNames];
-[UIInputContextHistory recipientIdentifiers];
-[UIInputContextHistory addTextEntry:timestamp:senderIdentifier:entryIdentifier:];
-[UIInputContextHistory initWithRecipientIdentifiers:];
-[UIInputContextHistory initWithRecipientIdentifiers:senderIdentifier:];
-[UIInputContextHistory mostRecentTextEntries:];
-[UIInputContextHistory tiInputContextHistory];
-[UIInputContextHistory addNewParticipantWithIdentifier:name:];
-[UIInputContextHistory addTextEntry:timestamp:senderIdentifier:];
-[UIInputContextHistory isEqual:];
-[UIInputContextHistory addTextEntry:timestamp:];
-[UIInputContextHistory senderIdentifier];
-[UIInputContextHistory initWithRecipientIdentifiers:senderIdentifiers:];
-[UIInputContextHistory didFinishAddingEntriesToInputContextHistory];
-[UIInputContextHistory initWithInputContextHistory:];
-[UIInputContextHistory initWithThreadID:participantsIDtoNamesMap:firstPersonIDs:primaryRecipients:secondaryRecipients:infoDict:];
-[UIInputContextHistory initWithThreadIdentifier:participantsIDtoNames:firstPerson:primaryRecipients:secondaryRecipients:info:];
```
