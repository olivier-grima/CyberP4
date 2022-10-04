CC = gcc
CC_FLAGS = -Wall 

# File names
SOURCES = strat_jeu.c
OBJECTS = $(SOURCES:module.c=.so)

# Main target
all: $(OBJECTS)

# Object files
%.so: %module.c
	$(CC) $(CC_FLAGS) $< -o $@

run: $(OBJECTS)
	python3 -c "import somme; somme.sommefunc('Foobar')"

# To remove generated files
clean:
	rm -f *.so

.PHONY: all run clean
//////////////////////////
SRC = main.c callbacks.c modele.c vue.c # les fichiers sources
PROG = jeu_de_la_vie # nom de l’exécutable
OBJS = $(SRC:.c=.o) # les .o qui en découlent
.SUFFIXES: .c .o # lien entre les suffixes

#règles
all: $(PROG)

# étapes de compilation et d’édition de liens
# $@ la cible $^ toutes les dépendances
$(PROG): $(OBJS)
	$(CC) -o $@ $^ $(LDFLAGS)

callbacks.o: callbacks.h modele.h vue.h
modele.o: modele.h
main.o: vue.h modele.h
vue.o : modele.h callbacks.h
# le lien entre .o et .c
# $< dernière dépendance
%.o: %.c
	$(CC) $(CFLAGS) -c $<

# pour faire propre
.PHONY: clean
clean:
	rm −f *.o *~ core $(PROG)