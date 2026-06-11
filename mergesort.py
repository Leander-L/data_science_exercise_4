# Änderung: import Statement nach oben für Übersicht im Code
import matplotlib.pyplot as plt

# Änderung: ASSIGNMENT ist überflüssig, da es die Zuweisung nur unnötig kompliziert macht

# Änderung: Parameter in unsorted_list umbenannt: gleiche Bedeutung, aber weniger Zeichen und einfacher zu lesen als list_to_be_sorted_by_merge
# Änderung: umbenannt in merge_sort --> alles klein und mit Unterstrich zwischen den Worten
def merge_sort(unsorted_list):
    # Änderung: Abfrage zur Länge der Liste in eine Anfrage gebündelt + return, wenn Länge <= 1, um nicht die eigentlichen Anweisungen der Funktion unter Bedingung zu stellen --> übersichtlicher
    # Basisfall: übergebene Liste hat 1 oder kein Argument und muss/kann nicht mehr geteilt werden
    if (len(unsorted_list) <= 1):
        return
    
    # Aufteilung der Listen in n/2 links und ab n/2 rechts
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    # Rekursiver Aufruf
    merge_sort(left)
    merge_sort(right)

    # Index Initialisierung für links, rechts und zu sortierender Liste
    index_left = 0
    index_right = 0
    index_to_place = 0

    # Änderung: da die Länge mehrfach für Abfragen benötigt wird, kann man sie auch in einer Variable Speichern, um Funktionsaufrufe zu verringern
    length_left = len(left)
    length_right = len(right)

    # Entlang der sortierten linken und rechten Liste gehen und mittels Vergleich nacheinander in die Ausgangsliste kopieren (inplace Operation sozusagen) 
    while index_left < length_left and index_right < length_right:
        if left[index_left] <= right[index_right]:
            unsorted_list[index_to_place] = left[index_left] # Änderung: hier wurde einfache Zuweisung statt Assignment hinzugefügt
            index_left += 1
        else:
            unsorted_list[index_to_place] = right[index_right] # Änderung: hier wurde einfache Zuweisung statt Assignment hinzugefügt
            index_right += 1
        index_to_place += 1

    # Restliche Elemente der Liste kopieren, die länger als die andere gewesen ist  
    while index_left < length_left:
        unsorted_list[index_to_place] = left[index_left]
        index_left += 1
        index_to_place += 1

    while index_right < length_right:
        unsorted_list[index_to_place] = right[index_right]
        index_right += 1
        index_to_place += 1

# Änderung: Programm in einer main-Funktion bündeln, um besser zwischen den Funktionen zu trennen
def main():
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("unsortierte Liste: " + str(my_list)) # Keine direkte Änderung, sondern eher für die Kontrolle, dass der Code von mergeSort noch dasselbe macht
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()
    merge_sort(my_list)
    print("sortierte Liste: " + str(my_list)) # Keine direkte Änderung, sondern eher für die Kontrolle, dass der Code von mergeSort noch dasselbe macht
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()

# Notwendig, damit beim Datei-Start auch die main ausgeführt wird
if __name__ == "__main__":
    main()
