#!/usr/bin/env python

# Frappe 0.9.0
# Copyright 2009-2010 Meadow Hill Software
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygtk
pygtk.require("2.0")
import gtk
def createButton(label):
	button = gtk.Button(label)
	button.show()
	return button

class Frappe:
	def __init__(self):
		self.window = gtk.Dialog("~Frappe~")
		self.window.connect("delete_event", gtk.main_quit, False)
		self.ok = createButton("OK")
		self.ok.connect("clicked", gtk.main_quit, False)
		self.cancel = createButton("Cancel")
		self.cancel.connect("clicked", gtk.main_quit, False)
		self.window.action_area.pack_start(self.ok, True, True, 0)
		self.window.action_area.pack_start(self.cancel, True, True, 0)
		self.table = gtk.Table(20, 5)
		self.window.vbox.pack_start(self.table, False, False, 0)
		self.label = gtk.Label("Number of dice:   ")
		self.table.attach(self.label, 0, 1, 0, 1)
		self.dice = gtk.Entry()
		self.table.attach(self.dice, 1, 2, 0, 1)
		self.enter = createButton("Enter")
		self.enter.connect("clicked", self.calculateOdds, None)
		self.table.attach(self.enter, 2, 3, 0, 1)
		self.export = createButton("Export")
		self.export.connect("clicked", self.exportInfo, None)
		self.table.attach(self.export, 3, 4, 0, 1)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 0, 1)
		self.label = gtk.Label("Combinations")
		self.table.attach(self.label, 0, 5, 1, 2)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 2, 3)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 3, 4)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 4, 5)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 5, 6)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 6, 7)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 7, 8)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 8, 9)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 9, 10)
		self.combo_window = gtk.ScrolledWindow()
		self.combo_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.table.attach(self.combo_window, 0, 4, 2, 10)
		self.combinations = gtk.TextView()
		self.combinations.set_wrap_mode(gtk.WRAP_WORD)
		self.combinations.set_justification(gtk.JUSTIFY_LEFT)
		self.combinations.set_editable(False)
		self.combinations.set_cursor_visible(False)
		self.combinations_buffer = self.combinations.get_buffer()
		self.combo_window.add(self.combinations)
		self.label = gtk.Label("Percentages")
		self.table.attach(self.label, 0, 5, 10, 11)
		self.percent_window = gtk.ScrolledWindow()
		self.percent_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		self.table.attach(self.percent_window, 0, 4, 11, 19)
		self.percentages = gtk.TextView()
		self.percentages.set_wrap_mode(gtk.WRAP_WORD)
		self.percentages.set_justification(gtk.JUSTIFY_LEFT)
		self.percentages.set_editable(False)
		self.percentages.set_cursor_visible(False)
		self.percentages_buffer = self.percentages.get_buffer()
		self.percent_window.add(self.percentages)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 11, 12)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 12, 13)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 13, 14)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 14, 15)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 15, 16)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 16, 17)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 17, 18)
		self.label = gtk.Label("")
		self.table.attach(self.label, 4, 5, 18, 19)
		self.window.show_all()
		self.combos = ""
		self.percents = ""

	def calculateOdds(self, widget, data = None):
		dice = self.dice.get_text()
		dice = int(dice)
		combinations = []
		set = [1, 2, 3, 4, 5, 6]
		successes = {0: 4, 1: 2}
		adders = {}
		if dice > 0:
			old = {}
			keys = successes.keys()
			keys.sort()
			for num in range(1, dice):
				for key in keys:
					multiple = successes[key] * 6
					quotient = multiple / 3
					difference = multiple - quotient
					successes[key] = difference
					adders[(key + 1)] = quotient
				for key in adders.keys():
					if key in successes.keys():
						successes[key] += adders[key]
					else:
						successes[key] = adders[key]
						keys = successes.keys()
						keys.sort()
			keys = successes.keys()
			keys.sort()
			total = 0
			for key in keys:
				total += successes[key]
			combos = "Total number of possible combinations: %d\n" % total
			for key in keys:
				combos = combos + "Number of possible combinations with %d successes: %d\n" % (key, successes[key])
			self.combos = combos[:]
			self.combinations_buffer.set_text(combos)
			percents = ""
			for key in keys:
				percents = percents + "Chance of %d successes: %.10f percent\n" % (key, ((successes[key] * 100) / float(total)))
			self.percentages_buffer.set_text(percents)
			self.percents = percents[:]

	def exportInfo(self, widget, data = None):
		if self.combos != "":
			odds = file("Fringe-Probabilities.txt", "w")
			odds.write(self.combos + "\n" + self.percents)
			odds.close()
			self.combinations_buffer.set_text(self.combos + "\nData exported to Fringe-Probabilities.txt")
			self.percentages_buffer.set_text(self.percents + "\nData exported to Fringe-Probabilities.txt")
		else:
			self.combinations_buffer.set_text("No data to export")
			self.percentages_buffer.set_text("No data to export")			

def main():
	gtk.main()

if __name__ == "__main__":
	frappe = Frappe()
	main()
		
