import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import javax.swing.*;
import javax.swing.event.ChangeListener;
import javax.swing.event.ChangeEvent;

import java.awt.event.MouseEvent;
import java.awt.event.MouseAdapter;

public class GUI {
	
	private static JFrame frame;
	
	//Define variables.
	static String currentYear = "2016";
	static String CobolVersion = "Cobol_410";
	static String CVersion = "C_408";
	static String PLSQLVersion = "plsql410";
	/**
	static String VMname = "devsrv006";
	static String CobolInfo = "//"+VMname+"/L/"+CobolVersion;
	static String CInfo = "//"+VMname+"/L/"+CVersion;
	static String PLSQLInfo = "//"+VMname+"/L/taxtestutl";
	static String currentPLSQLFolder = "//"+VMname+"/L/"+PLSQLVersion;
	*/
	static String currentNoMonth[] = new String[] {"1","2","3","4","5","6","7","8","9","10","11","12"};

	static String orderPartialPath[] = new String[] {"Prior","Functional","Regression"}; //Think folders
	static String updateGenerateFolder[] = new String[] {"1.101\\1.101.12.P"};
	static String updateTypePartialPath[] = new String[] {"Regular","Backfill"};
	private static JTextField textField;
	static String storeAllString = "";
	
	static File selectedFile = null;
	
	private static void createAndShowGUI() {
		
		String labels[] = { "Prior Master Files", "Current Update Files", "Regression Incremental Package", "Regression Full Package" };
		String testcases[] = {"C:/Users/jeffrey.thomas/Results/Data/LOADING_PRIOR_MASTER.cmd", "C:/Users/jeffrey.thomas/Results/Data/LOADING_CURRENT_UPDATE.cmd",
				"C:/Users/jeffrey.thomas/Results/Data/LOADING_REGRESSION_INC_0.cmd", "C:/Users/jeffrey.thomas/Results/Data/LOADING_REGRESSION_FULL.cmd"};
		String defaultDirectory = "C:/Miniconda2/Lib/site-packages";
		
		
		frame = new JFrame("SUT Load");
		frame.setForeground(Color.BLACK);
		frame.getContentPane().setFont(new Font("Tahoma", Font.BOLD, 11));
		frame.setResizable(false);
		frame.setBounds(200,200,700,357);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		//frame.add(new JLabel(new ImageIcon("C:\\Users\\jeffrey.thomas\\Pictures\\dolphins.jpg")));
		
		JButton PMFiles = new JButton(labels[0]);
		PMFiles.setBounds(10, 30, 150, 23);
		frame.getContentPane().add(PMFiles);
		
		Component verticalGlue = Box.createVerticalGlue();
		verticalGlue.setBounds(574, 66, 0, -13);
		frame.getContentPane().add(verticalGlue);
		
		JButton CUFiles = new JButton(labels[1]);
		CUFiles.setBounds(10, 66, 150, 23);
		frame.getContentPane().add(CUFiles);
		
		JButton Inc = new JButton(labels[2]);
		Inc.setBounds(10, 100, 230, 23);
		frame.getContentPane().add(Inc);
		
		JButton Full = new JButton(labels[3]);
		Full.setBounds(10, 134, 186, 23);
		frame.getContentPane().add(Full);
		
		JButton vfButton = new JButton("...");
		
		JComboBox<String> cNM = new JComboBox<String>();
		cNM.setEditable(true);
		cNM.setModel(new DefaultComboBoxModel<String>(currentNoMonth));
		cNM.setBounds(330, 42, 37, 23);
		frame.getContentPane().add(cNM);
		
		JComboBox<String> oPP = new JComboBox<String>();
		oPP.setEditable(true);
		oPP.setModel(new DefaultComboBoxModel<String>(orderPartialPath));
		oPP.setBounds(330, 140, 120, 23);
		frame.getContentPane().add(oPP);
		
		JComboBox<String> uGF = new JComboBox<String>();
		uGF.setEditable(true);
		uGF.setModel(new DefaultComboBoxModel<String>(updateGenerateFolder));
		uGF.setBounds(330, 91, 120, 20);
		frame.getContentPane().add(uGF);
		
		JComboBox<String> uTPP = new JComboBox<String>();
		uTPP.setEditable(true);
		uTPP.setModel(new DefaultComboBoxModel<String>(updateTypePartialPath));
		uTPP.setBounds(330, 189, 120, 20);
		frame.getContentPane().add(uTPP);
		
		textField = new JTextField();
		JFileChooser chooser = new JFileChooser(defaultDirectory);
		chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
		
		//Select user's variable file.
		vfButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				File selectedDir = null;
				String absPath = null;
				int returnValue = chooser.showOpenDialog(textField);
				if (returnValue == JFileChooser.APPROVE_OPTION) {
					selectedFile = chooser.getSelectedFile();
					absPath = chooser.getSelectedFile().getAbsolutePath();
					selectedDir = chooser.getCurrentDirectory();
					textField.setText(absPath);
					//System.out.println(selectedDir);
					if (selectedDir != null) {
						chooser.setCurrentDirectory(selectedDir);
					}
					chooser.setCurrentDirectory(selectedDir);
				}

				String varfile = textField.getText();
			}
		});
		textField.setBounds(10, 225, 223, 20);
		frame.getContentPane().add(textField);
		textField.setColumns(10);
		
		JCheckBox chckbxNewCheckBox = new JCheckBox("Is this a Supplemental?");
		chckbxNewCheckBox.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (chckbxNewCheckBox.isSelected()) {
					ContextMenu context = new ContextMenu();
				}
			}
		});
		chckbxNewCheckBox.setBounds(512, 30, 165, 23);
		frame.getContentPane().add(chckbxNewCheckBox);
		
		JCheckBox chckbxNewCheckBox_1 = new JCheckBox("Using Test Evironment?");
		chckbxNewCheckBox_1.setBounds(512, 66, 165, 23);
		frame.getContentPane().add(chckbxNewCheckBox_1);
		
		JCheckBox chckbxNewCheckBox_2 = new JCheckBox("Working on Backfill?");
		chckbxNewCheckBox_2.setBounds(512, 100, 165, 23);
		frame.getContentPane().add(chckbxNewCheckBox_2);
		
		
		vfButton.setBounds(236, 226, 37, 18);
		frame.getContentPane().add(vfButton);
		
		JButton setVarFileBtn = new JButton();
		JLabel vfBottomLabel = new JLabel("SET VARIABLES");
		vfBottomLabel.setBackground(Color.DARK_GRAY);
		setVarFileBtn.add(vfBottomLabel);
		
		setVarFileBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent a) {
				
				FileWriter write;
				try {
				    write = new FileWriter(selectedFile,true);
				    BufferedWriter bufferFileWriter = new BufferedWriter(write);
				    
				    String cNMline = (String) cNM.getSelectedItem();
				    String oPPline = (String) oPP.getSelectedItem();
				    String uGFline = (String) uGF.getSelectedItem();
				    String uTPPline = (String) uTPP.getSelectedItem();
				    
				    bufferFileWriter.write("currentNoMonth = \""+cNMline+"\"");
				    bufferFileWriter.newLine();
				    bufferFileWriter.write("orderPartialPath = \""+oPPline+"\"");
				    bufferFileWriter.newLine();
				    bufferFileWriter.write("updateGenerateFolder = \""+uGFline+"\"");
				    bufferFileWriter.newLine();
				    bufferFileWriter.write("updateTypePartialPath = \""+uTPPline+"\"");
				    bufferFileWriter.newLine();
				    bufferFileWriter.close();
				} catch (IOException e) {
					e.printStackTrace();
				    //Logger.getLogger(JsonTest.class.getName()).log(Level.SEVERE, null, e);
				}
			}
		});

		setVarFileBtn.setBounds(325, 223, 130, 23);
		frame.getContentPane().add(setVarFileBtn);
		
		Label label = new Label("Select your variable file");
		label.setFont(new Font("Dialog", Font.BOLD, 12));
		label.setBounds(10, 203, 150, 22);
		frame.getContentPane().add(label);
		
		Label label_1 = new Label("Month (digit)");
		label_1.setFont(new Font("Dialog", Font.BOLD, 12));
		label_1.setBounds(330, 22, 150, 18);
		frame.getContentPane().add(label_1);
		
		Label label_2 = new Label("Generate Folder");
		label_2.setFont(new Font("Dialog", Font.BOLD, 12));
		label_2.setBounds(330, 71, 150, 18);
		frame.getContentPane().add(label_2);
		
		Label label_3 = new Label("Update Stage");
		label_3.setFont(new Font("Dialog", Font.BOLD, 12));
		label_3.setBounds(330, 120, 150, 18);
		frame.getContentPane().add(label_3);
		
		Label label_4 = new Label("Update Type");
		label_4.setFont(new Font("Dialog", Font.BOLD, 12));
		label_4.setBounds(330, 169, 150, 18);
		frame.getContentPane().add(label_4);
		
		PMFiles.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				if (event.getSource() == PMFiles) {
					runSUTLoad.runSUTLoad1(testcases[0]);
				}
			}
		});
		
		CUFiles.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				if (event.getSource() == CUFiles) {
					runSUTLoad.runSUTLoad1(testcases[1]);
				}
			}
		});
		
		Inc.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				if (event.getSource() == Inc) {
					runSUTLoad.runSUTLoad1(testcases[2]);
				}
			}
		});
		
		Full.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				if (event.getSource() == Full) {
					runSUTLoad.runSUTLoad1(testcases[3]);
				}
			}
		});
		
        frame.setVisible(true);
	}
	
	public static void main(String[] args) {
		javax.swing.SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				createAndShowGUI();
			}
		});
	}
}
